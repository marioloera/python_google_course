"""
We're using the same syslog, 
and we want to display the date, time, and process id 
that's inside the square brackets. 
We can read each line of the syslog and pass the
 contents to the show_time_of_pid function. 
 Fill in the gaps to extract the date, time, 
 and process id from the passed line, 
 and return this format: Jul 6 14:01:23 pid:29440.

"""

import re
def show_time_of_pid(line):

    pattern = r'(\d*:\d*:\d*)' # time
    pattern = r'^(\w* \d*)' # date
    pattern = r'\[(\d*)\]' # pid

    pattern = r'^(\w* \d* \d*:\d*:\d*)' # date,time

    pattern = r'^(\w* \d* \d*:\d\d:\d\d) .* \[(\d*)\]'
    pattern = r'^(\w* \d* \d*:\d*:\d*).*\[(\d*)\].*$' # date,time

    newformat = r"\1 pid:\2"
    #     return result
    result = re.search(pattern, line)
    l = "{ts} pid:{pid}".format(ts=result[1], pid=result[2])

    print('1:'+l)

    #print(result[1])

    #print(result[2])
    #print(result)
    l = re.sub(pattern, newformat, line)
    print('2:'+l)
    return l

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440