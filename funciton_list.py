#!/usr/bin/env python3
import random
import sys

def func1():
    return bool(random.randint(0,1))
    # return True 

def some_other_fun():
    return bool(random.randint(0,1))
    # return True

def main():
    checks = [
            (func1, 'error at func1'),
            (some_other_fun, 'error at some_other_fun')
            ]

    everything_ok = True
    
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if everything_ok:
        print('Everything ok')
        sys.exit(0)

    else:
        sys.exit(1)

main()