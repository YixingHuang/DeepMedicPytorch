import torch.nn as nn
import torch.nn.functional as F
import math
import torch

# adapt from https://github.com/Kamnitsask/deepmedic

class ResBlock(nn.Module):
    def __init__(self, inplanes, planes):
        super(ResBlock, self).__init__()
        self.inplanes = inplanes
        self.conv1 = nn.Conv3d(inplanes, planes, 3, bias=False)
        self.bn1 = nn.BatchNorm3d(planes)
        self.conv2 = nn.Conv3d(planes, planes, 3, bias=False)
        self.bn2 = nn.BatchNorm3d(planes)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        y = self.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))
        x = x[:, :, 2:-2, 2:-2, 2:-2]
        y[:, :self.inplanes] += x
        y = self.relu(y)
        return y

def conv3x3(inplanes, planes, ksize=3):
    return nn.Sequential(
            nn.Conv3d(inplanes, planes, ksize, bias=False),
            nn.BatchNorm3d(planes),
            nn.ReLU(inplace=True))

def repeat(x, n=3):
    # nc333
    b, c, h, w, t = x.shape
    x = x.unsqueeze(5).unsqueeze(4).unsqueeze(3)
    x = x.repeat(1, 1, 1, n, 1, n, 1, n)
    return x.view(b, c, n*h, n*w, n*t)


class DeepMedic(nn.Module):
    def __init__(self, c=4, n1=30, n2=40, n3=50, m=150, up=True, cout=5):
        super(DeepMedic, self).__init__()
        #n1, n2, n3 = 30, 40, 50

        n = 2*n3

        self.branch1 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                ResBlock(n1, n2),
                ResBlock(n2, n2),
                ResBlock(n2, n3))

        self.branch2 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                conv3x3(n1, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n3),
                conv3x3(n3, n3))

        self.up3 = nn.Upsample(scale_factor=3,
                mode='trilinear', align_corners=False) if up else repeat

        self.fc = nn.Sequential(
                conv3x3(n, m, 1),
                conv3x3(m, m, 1),
                nn.Conv3d(m, cout, 1))

        for m in self.modules():
            if isinstance(m, nn.Conv3d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm3d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, inputs):
        # Debugging for the strides.
        # print(x1.shape, x1.stride())
        # desired_strides = (15625, 15625, 625, 25, 1)
        # x1 = torch.as_strided(x1, size=x1.size(), stride=desired_strides)
        # print(x1.shape, x1.stride())
        # with torch.autograd.profiler.profile() as prof:
        # x1 = self.start1(x1)
        #     print(x1.shape, x1.stride())
        # print(prof.key_averages().table(sort_by="count"))
        # x2 = self.start2(x2)

        x1, x2 = inputs
        x1 = self.branch1(x1)
        x2 = self.branch2(x2)
        x2 = self.up3(x2)
        x = torch.cat([x1, x2], 1)
        x = self.fc(x)
        return x


class DeepMedicWide(nn.Module):
    def __init__(self, c=4, n1=30, n2=40, n3=50, m=150, up=True, cout=5):
        super(DeepMedicWide, self).__init__()
        #n1, n2, n3 = 30, 40, 50

        n = 2*n3

        self.branch1 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                ResBlock(n1, n2),
                ResBlock(n2, n2),
                ResBlock(n2, n3))

        self.branch2 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                conv3x3(n1, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n3),
                conv3x3(n3, n3))

        self.branch3 = nn.Sequential(
            conv3x3(c, n1),
            conv3x3(n1, n1),
            conv3x3(n1, n2),
            conv3x3(n2, n2),
            conv3x3(n2, n2),
            conv3x3(n2, n2),
            conv3x3(n2, n3),
            conv3x3(n3, n3))

        self.up3 = nn.Upsample(scale_factor=3,
                mode='trilinear', align_corners=False) if up else repeat

        self.fc = nn.Sequential(
                conv3x3(n, m, 1),
                conv3x3(m, m, 1),
                nn.Conv3d(m, cout, 1))

        for m in self.modules():
            if isinstance(m, nn.Conv3d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm3d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, inputs):

        x1, x2, x3 = inputs
        x1 = self.branch1(x1)
        x2 = self.branch2(x2)
        x3 = self.branch3(x3)
        x2 = self.up3(x2)
        x = torch.cat([x1, x2], 1)
        x = self.fc(x)
        return x


class VDeepMedic(nn.Module):
    def __init__(self, c=4, n1=30, n2=40, n3=50, m=150, up=True, cout=5):
        super(VDeepMedic, self).__init__()
        #n1, n2, n3 = 30, 40, 50
        # need 29 inputs

        n = 2*n3
        self.branch1 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                ResBlock(n1, n2),
                ResBlock(n2, n2),
                ResBlock(n2, n2),
                ResBlock(n2, n2),
                ResBlock(n2, n3))

        self.branch2 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                conv3x3(n1, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n3),
                conv3x3(n3, n3))

        self.up3 = nn.Upsample(scale_factor=3,
                mode='trilinear', align_corners=False) if up else repeat

        self.fc = nn.Sequential(
                conv3x3(n, m, 1),
                conv3x3(m, m, 1),
                nn.Conv3d(m, cout, 1))

        for m in self.modules():
            if isinstance(m, nn.Conv3d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm3d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, inputs):
        x1, x2 = inputs
        x1 = self.branch1(x1)
        x2 = self.branch2(x2)
        x2 = self.up3(x2)
        x = torch.cat([x1, x2], 1)
        x = self.fc(x)
        return x


# no residual connections
class DeepMedicNR(nn.Module):
    def __init__(self, c=4, n1=30, n2=40, n3=50, m=150, up=True, cout=5):
        super(DeepMedicNR, self).__init__()
        #n1, n2, n3 = 30, 40, 50

        n = 2*n3
        self.branch1 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                conv3x3(n1, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n3),
                conv3x3(n3, n3))

        self.branch2 = nn.Sequential(
                conv3x3(c, n1),
                conv3x3(n1, n1),
                conv3x3(n1, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n2),
                conv3x3(n2, n3),
                conv3x3(n3, n3))

        self.up3 = nn.Upsample(scale_factor=3,
                mode='trilinear', align_corners=False) if up else repeat

        self.fc = nn.Sequential(
                conv3x3(n, m, 1),
                conv3x3(m, m, 1),
                nn.Conv3d(m, cout, 1))

        for m in self.modules():
            if isinstance(m, nn.Conv3d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm3d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, inputs):
        x1, x2 = inputs
        x1 = self.branch1(x1)
        x2 = self.branch2(x2)
        x2 = self.up3(x2)
        x = torch.cat([x1, x2], 1)
        x = self.fc(x)
        return x

#import torch
#x1 = torch.rand(100, 4, 25, 25, 25)
#x2 = torch.rand(100, 4, 19, 19, 19)
#
#x1, x2 = x1.cuda(), x2.cuda()
#model = Model().cuda()
#x = model((x1, x2))
#print(x.size())
