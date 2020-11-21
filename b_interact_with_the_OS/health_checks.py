#!/usr/bin/env python3
import shutil #disk usage
import psutil #procesor ussage
from network import *

def check_disk_usage(disk):
    """Check the usage of a given disk, return True if at least 20 is free """
    du = shutil.disk_usage(disk)
    free = du.free/du.total
    return free >= .2


def check_cpu_usage():
    """Check the cpu usage return True if is less 75% """
    usage = psutil.cpu_percent(.1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR!')

elif check_localhost() and check_connectivity():
    print("Everything ok")

else:
    print("Network checks failed")


# adding  execute permission (x) in linux
# sudo chmod +x health_checks.py