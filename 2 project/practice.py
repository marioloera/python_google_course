#!/usr/bin/env python3

import re
import operator

def getinfo(line):
    regex = r"ticky: INFO: ([\w ]*).*\((\w.*)\)" #with user name
    regex = r"ticky: INFO: ([\w ]*) "
    result = re.findall(regex, line)
    print(result)
    pass


def geterror(line):
    regex = r"ticky: ERROR: ([\w ]*) "
    regex = r"ticky: ERROR: ([\w ]*).*\((\w.*)\)" #with user name
    result = re.findall(regex, line)
    print(result)
    pass


def get_log_info(line):
    regex = r"ticky: (\w*): ([\w ]*).* \((\w.*)\)" #with user name
    result = re.findall(regex, line)
    print(result)
    print(result[0])
    print(type(result[0]))
    event = None
    info = None
    user = None
    if len(result[0]) == 3:
        event = result[0][0]
        info = result[0][1]
        user = result[0][2]
        print(event, info, user)
    return event, info, user


def dic():
    fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
    print(fruit)
    print(sorted(fruit.items(), key=operator.itemgetter(1), reverse=True))


def main():
    line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
    getinfo(line)
    line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
    dic()
    geterror(line)
    event, info, user = get_log_info(line)
    #print(event, info, user)

main()