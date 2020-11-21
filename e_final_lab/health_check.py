#!/usr/bin/env python3
import os
import sys
import psutil
import shutil
import socket
import emails


def  main():
    sender = 'automation@example.com'
    receiver = '{}@example.com'.format(os.environ.get('USER'))
    body = 'Please check your system and resolve the issue as soon as possible.'
    subject = '*****_T_E_S_T_*****'
    message = emails.generate(sender, receiver, subject, body)
    print(message)
    #emails.sent(message)

    checks = [
        (check_localhost, 'Error - localhost cannot be resolved to 127.0.0.1'),
        (check_disk, 'Error - Available disk space is less than 20%'),
        (check_cpu_usage, 'Error - CPU usage is over 80%'),
        (check_ram, 'Error - Available memory is less than 500MB'),
    ]

    for check, msg in checks:
        if check():
            message = emails.generate(sender, receiver, msg, body)
            print(message)
            #emails.send(message)



def check_ram():
    free_mem = dict(psutil.virtual_memory()._asdict())['free'] / 2**20
    if free_mem < 500:
        return True
    return False


def check_disk():
    """Returns 
        True if there isn't enough disck space,
        False otherwhise.  """
    du = shutil.disk_usage('/')
    percent_free = 100 * du.free / du.total
    if percent_free < 0.20:
        return True
    return False


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'


def check_cpu_usage():
    """Check the cpu usage return True if is more 80% """
    usage = psutil.cpu_percent(.1)
    return usage > 80


if __name__ == '__main__':
    main()
