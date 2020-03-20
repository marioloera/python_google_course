"""
Let's say we have a text file containing current visitors at
 a hotel. We'll call it, guests.txt. Run the following code
  to create the file. The file will automatically populate 
  with each initial guest's first name on its own line.
"""
def print_guest():
    with open("guests.txt") as guests:
        [print(line.strip()) for line in guests]

initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
guests = open("guests.txt", "w")
for i in initial_guests:
    guests.write(i + "\n")   
guests.close()

"""
Now suppose we want to update our file 
as guests check in and out. Fill in the missing 
code in the following cell to add guests to the 
guests.txt file as they check in.
"""
new_guests = ["Sam", "Danielle", "Jacob"]
with open("guests.txt", "a") as guests:
    for new_guest in new_guests:
        guests.write(new_guest + "\n")
#guests.close()

"""
Now let's remove the guests that have checked out already. 
There are several ways to do this, however, 
the method we will choose for this exercise is 
outlined as follows:

Open the file in "read" mode.
Iterate over each line in the file and put each 
guest's name into a Python list.
Open the file once again in "write" mode.
Add each guest's name in the Python list to 
the file one by one.
"""

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

"""
Now let's check whether Bob and Andrea are 
still checked in. How could we do this? We'll 
just read through each line in the file to see 
if their name is in there. Run the following code 
to check whether Bob and Andrea are still checked in.
"""
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))
#print_guest()

import os
import datetime

ts = os.path.getmtime("guests.txt")
print(ts)
d = datetime.datetime.fromtimestamp(ts)
print(d)



