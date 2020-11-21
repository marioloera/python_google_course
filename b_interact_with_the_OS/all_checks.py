#!/usr/bin/env python3
import os
import sys
import psutil
import shutil
import socket
import requests

def main():

    checks = [
        (check_localhost, 'Error - localhost cannot be resolved to 127.0.0.1'),
        (check_disk, 'Error - Available disk space is less than 20%'),
        (check_cpu_usage, 'Error - CPU usage is over 80%'),
        (check_ram, 'Error - Available memory is less than 500MB'),
        # extra checks
        (check_root_full, 'Root partition full.'),
        (check_reboot, 'Pending Reboot.'),
    ]
    
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
    
    if not everything_ok:
        sys.exit(1)
    
    print('Everything ok.')
    sys.exit(0)

    # call each check at the time, a lot of code repetetion
    # if check_reboot():
    #     print('Pending Reboot.') 
    #     sys.exit(1)

    # if check_root_full():
    #     print('Root partition full.')
    #     sys.exit(1)

def check_ram():
    x = psutil.virtual_memory()
    # you can convert that object to a dictionary 
    free_mem = dict(psutil.virtual_memory()._asdict())['free'] / 2**20
    if free_mem < 500:
        return True
    return False
    # # you can have the percentage of used RAM
    # psutil.virtual_memory().percent
    # 79.2
    # # you can calculate percentage of available memory
    # psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    # 20.8


def check_disk():
    """Returns 
        True if there isn't enough disck space,
        False otherwhise.  """
    du = shutil.disk_usage('/')
    percent_free = 100 * du.free / du.total
    if percent_free < 0.20:
        return True
    return False


def check_reboot():
    return os.path.exists('/run/reboot-required')


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'


def check_cpu_usage():
    """Check the cpu usage return True if is more 80% """
    usage = psutil.cpu_percent(.1)
    return usage > 80


# extra checks
def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk= '/', min_gb=2, min_percent=20)


def check_disk_full(disk, min_gb, min_percent):
    """Returns 
        True if there isn't enough disck space,
        False otherwhise.  """
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gb_free = du.free / 2**30
    if gb_free < min_gb or percent_free < min_percent:
        return True
    return False


def check_connectivity():
    request = requests.get("http://www.google.com")
    return request.status_code == 200


if __name__ == "__main__":
    main()        