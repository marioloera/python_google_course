print('module')

import random
import datetime

for i in range(10):
    print(random.randint(1, 10))

timestamp = datetime.datetime.now()
print(timestamp)
print(type(timestamp))
print(timestamp.year)
print(timestamp + datetime.timedelta(days=28))