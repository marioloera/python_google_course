import datetime
import pytz


# timezone = pytz.timezone("Etc/Greenwich")
timezone = pytz.timezone("UTC")

timestamp_string = '1990-03-29 11:22:33.444'
#timestamp_string = "1970-01-01 00:00:00"
dt0 = datetime.datetime.fromisoformat(timestamp_string)

#timestamp_string = '1990-03-29 11:22:33.444 UTC'
#dt0 = datetime.datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f %Z')
dt = timezone.localize(dt0)
print('dt:\n', dt)
print('timezone info:\n', dt.tzinfo)


ts =  datetime.datetime.timestamp(dt)
print('ts:\n', ts)



sec = 638709753.444
print('sec:\n', sec)
date_str_computerTimezone = datetime.datetime.fromtimestamp(sec)
date_str = datetime.datetime.utcfromtimestamp(sec)
print('date_str:\n', date_str)
