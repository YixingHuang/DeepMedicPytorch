import torch.nn.functional as F
import torch

# for metric code: https://github.com/MIC-DKFZ/BraTS2017/blob/master/utils_validation.py

cross_entropy = F.cross_entropy


def hard_cross_entropy(output, target, alpha=3.0):
    mtx = F.cross_entropy(output, target, reduce=False)

    bg = (target == 0)

    neg = mtx[bg]
    pos = mtx[1-bg]

    Np, Nn = pos.numel(), neg.numel()

    pos = pos.sum()

    k = min(Np*alpha, Nn)
    if k > 0:
        neg, _ = torch.topk(neg, int(k))
        neg = neg.sum()
    else:
        neg = 0.0

    loss = (pos + neg)/ (Np + k)

    return loss


def hard_per_im_cross_entropy(output, target, alpha=3.0):
    n, c = output.shape[:2]
    output = output.view(n, c, -1)
    target = target.view(n, -1)

    mtx = F.cross_entropy(output, target, reduce=False)

    pos = target > 0
    num_pos = pos.long().sum(dim=1, keepdim=True)

    loss = mtx.clone().detach()
    loss[pos] = 0
    _, loss_idx = loss.sort(1, descending=True)
    _, idx_rank = loss_idx.sort(1)

    num_neg = torch.clamp(alpha*num_pos, max=pos.size(1)-1)
    neg = idx_rank < num_neg

    return mtx[neg + pos].mean()


def focal_loss(output, target, alpha=0.25, gamma=2.0):
    n = target.size(0)

    lsfm = F.cross_entropy(output, target, reduce=False)

    pos = (target > 0).float()
    Np  = pos.view(n, -1).sum(1).view(n, 1, 1, 1)

    Np  = torch.clamp(Np, 1.0)
    z   = pos * alpha / Np / n  + (1.0 - pos) * (1.0 - alpha) / Np / n
    z   = z.detach()

    focal = torch.pow(1.0 - torch.exp(-lsfm), gamma) * lsfm * z

    return focal.sum()


def mean_cross_entropy(output, target, alpha=3.0):
    mtx = F.cross_entropy(output, target, reduce=False)

    bg = (target == 0)

    neg = mtx[bg]
    pos = mtx[1-bg]

    pos = pos.mean() if pos.numel() > 0 else 0
    neg = neg.mean() if pos.neg() > 0 else 0

    loss = (neg * alpha + pos)/(alpha + 1.0)
    return loss


eps = 0.1
def dice(output, target):
    num = 2*(output*target).sum() + eps
    den = output.sum() + target.sum() + eps
    return 1.0 - num/den


def cross_entropy_dice(output, target, weight=1.0):
    loss = weight * F.cross_entropy(output, target)
    output = F.softmax(output, dim=1)
    for c in range(1, 5):
        o = output[:, c]
        t = (target==c).float()
        loss += 0.25*dice(o, t)

    return loss


# in original paper: class 3 is ignored
# https://github.com/MIC-DKFZ/BraTS2017/blob/master/dataset.py#L283
# dice score per image per positive class, then aveg
def dice_per_im(output, target):
    n = output.shape[0]
    output = output.view(n, -1)
    target = target.view(n, -1)
    num = 2*(output*target).sum(1) + eps
    den = output.sum(1) + target.sum(1) + eps
    return 1.0 - (num/den).mean()


def cross_entropy_dice_per_im(output, target, weight=1.0):
    loss = weight * F.cross_entropy(output, target)
    output = F.softmax(output, dim=1)
    for c in range(1, 5):
        o = output[:, c]
        t = (target==c).float()
        loss += 0.25*dice_per_im(o, t)

    return loss


def jvss(y_predict, y_gt, alpha=0.95, eps=0.1, softmax=True, num_classes=2): #alpha value is not necessary.
    ce_loss = F.cross_entropy(y_predict, y_gt)
    # multiple channels as the output
    # y_predict: the output of the network;
    # y_gt: the ground truth classification labels
    # softmax: if True, apply softmax to convert y_predict to make the values in [0, 1] and sum to 1.
    # num_classes: number of classes to convert to one-hot coding
    # print('shape before 0', y_predict.shape, y_gt.shape)
    if softmax:
        y_predict = F.softmax(y_predict, dim=1)
    # print('shape aft softmax', y_predict.shape)
    y_gt = F.one_hot(y_gt, num_classes=num_classes)
    # print('shape before 1', y_predict.shape, y_gt.shape) #shape before 1 torch.Size([100, 2, 9, 9, 9]) torch.Size([100, 9, 9, 9, 2])
    Channel1_weighted_log_p_y_given_x_train = y_predict[:, 1, :, :, :]
    Channel1_y_one_hot = y_gt[:, :, :, :, 1] # the class channel is at the last dimension after one_hot conversion.  y_gt[:, 1, :, :, :]
    # print('shape', Channel1_weighted_log_p_y_given_x_train.shape, Channel1_y_one_hot.shape)
    product = Channel1_weighted_log_p_y_given_x_train * Channel1_y_one_hot
    maxprod = torch.amax(product, dim=(1,2,3))
    maxonehot = torch.amax(Channel1_y_one_hot, dim=(1,2,3))
    resultTP = torch.divide(torch.sum(maxprod), torch.sum(maxonehot) + eps)

    # True negatives
    Channel0_y_one_hot = y_gt[:, :, :, :, 0]# y_gt[:, 0, :, :, :]
    PatchesNegOneHot = torch.amax(Channel0_y_one_hot, dim=(1,2,3))
    MaxPrbNeg = torch.multiply(PatchesNegOneHot, torch.amax(Channel1_weighted_log_p_y_given_x_train, dim=(1,2,3)))
    resultTN = 1. - torch.divide(torch.sum(MaxPrbNeg), torch.sum(PatchesNegOneHot) + eps)
    # alpha = 0.5  # 0.995 for high sensitivity, 0.5 for high precision.
    # For your own data, a different alpha value may apply
    vss_loss = 1. - ((1 - alpha) * resultTN + alpha * resultTP)
    # print('vss cost', vss_loss.item(), 'Sensitivity', resultTP.item(), 'Specificity', resultTN.item())
    cost = ce_loss + vss_loss
    return cost


def knowledge_distillation_loss(student_output, teacher_output, temperature=2):

    # teacher_output and student_output are the output from the teacher and student models
    # alpha is the weight for the distillation loss
    # temperature is the temperature parameter for the distillation

    # Normalize the student's logits
    # print(student_output.size())
    student_output -= student_output.max(dim=1, keepdim=True)[0]

    # Normalize the teacher's logits
    teacher_output -= teacher_output.max(dim=1, keepdim=True)[0]
    # Calculate the hard target loss (with ground truth labels)
    # hard_loss = F.cross_entropy(student_output, y)

    # Calculate the soft target loss (with teacher's outputs)
    # We use the Kullback-Leibler Divergence loss (KLDivLoss)
    # Note: the teacher's output is detached as we don't want to backpropagate through it
    soft_loss = F.kl_div(F.log_softmax(student_output/temperature, dim=1),
                         F.softmax(teacher_output.detach()/temperature, dim=1),
                         reduction='batchmean')

    # return (1 - alpha) * hard_loss + (alpha * temperature * temperature) * soft_loss
    return soft_loss
