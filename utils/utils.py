import os

def check_system():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        if 'linux' in os.uname().sysname.lower():
            return 'Linux'
        else:
            return os.uname().sysname
    else:
        return 'Unknown'