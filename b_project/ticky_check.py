#!/usr/bin/env python3
import re
import operator


def get_file_lines(file):
    lines = []
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            lines.append(line.strip())
        f.close()
    return lines


def get_log_info(line):
    regex = r"ticky: (\w*) ([\w ]*).* \((\w.*)\)" #with user name
    print(line)
    print(regex)
    result = re.findall(regex, line)
    event = None
    info = None
    user = None
    if result != []:
        print(result)
        if len(result[0]) == 3:
            event = result[0][0]
            info = result[0][1]
            user = result[0][2]
    return event, info, user


def create_error_csv(data, filename):
    sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    with open(filename, 'w') as f:
        f.write('Error, Count')
        for error, count in sorted_data:
            line = '\n{e}, {c}'.format(e=error, c=count)
            f.write(line)
        f.close()


def create_user_csv(data, filename):
    sorted_data = sorted(data.items(), key=operator.itemgetter(0))
    with open(filename, 'w') as f:
        f.write('Username, INFO, ERROR')
        for user, d in sorted_data:
            line = '\n{u}, {i}, {e}'.format(u=user, i=d['INFO'], e=d['ERROR'])
            f.write(line)
        f.close()


def main():
    lines = get_file_lines('syslog.log')
    event_info = 'INFO'
    event_error = 'ERROR'
    error_message = {}
    user_statistics = {}

    for line in lines:
        event, info, user = get_log_info(line)
        
        if event not in [event_info, event_error]:
            continue

        if user not in user_statistics:
            user_statistics[user] = {event_info:0, event_error:0}

        if event == event_info:
            user_statistics[user][event_info] +=1

        if event == event_error:
            if info not in error_message:
                error_message[info] = 0
            error_message[info] += 1
            user_statistics[user][event_error] +=1

    create_error_csv(error_message, 'error_message.csv')
    create_user_csv(user_statistics, 'user_statistics.csv')


main()