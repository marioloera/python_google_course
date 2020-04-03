#!/usr/bin/env python3

import sys
import os
import re

def error_search(log_file):
    returned_errors = []
    error_patterns = ["error"]
    error = input("What is the error? ")
    for e in error.split(' '):
        error_patterns.append(r"{}".format(e.lower()))

    # for i in range(len(error.split(' '))):
    #     print(i)
    #     error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

    with open(log_file, mode='r', encoding='UTF-8') as f:
        for log in f.readlines():
            if all(re.search(regex, log.lower()) for regex in error_patterns):
                print(log)
                returned_errors.append(log)    
        f.close()
    return returned_errors

def file_output(file_output, returned_errors):
    with open(file_output, 'w') as out_f:
        for e in returned_errors:
            out_f.write(e)
        out_f.close()


if __name__ == "__main__":
    #log_file = sys.argv[1]
    log_file = 'fishy.log'

    output_file = 'errors_found.log'
    #output_file = os.path.expanduser('~') + '/data/' + output_file

    returned_errors = error_search(log_file)
    file_output(output_file, returned_errors)
    sys.exit(0)

