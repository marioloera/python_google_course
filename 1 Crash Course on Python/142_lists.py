
def group_list(group, users):
      return "{group}: {users_list}".format(group = group, users_list=", ".join(users))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def skip_elements(elements):
      result = []
      add = True
      for element in elements:
            if add:
                  result.append(element)
            add = not add
      return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

x = ['a','b']
y = ('a', 'b')

def print_info(a):
      m = '{t}: {data}'.format(t=type(a), data=a)
      print(m)

print_info(x)
print_info(y)

# prints the sentence "GuestName is X years old and works as __."
def guest_list(guests):
      for guest in guests:
            name, age, profession = guest
            text = "{name} is {age} years old and works as {profession}.".format(
                        name=name, age=age, profession=profession)
            print(text)

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

x = ['123','45']
m = ''.join(x)
print(len(m), len(m)/len(x))

def skip_elements(elements):
      # code goes here
      result = []
      for i, element in enumerate(elements):
            if i%2 == 0:
                  result.append(element)
      return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

fruits = ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']
print(fruits)
# list comprehension
fruits_len = [len(fruit) for fruit in fruits]
print(fruits_len)

def skip_elements(elements):
      # code goes here
      result = [element for i, element in enumerate(elements) if i%2 == 0]
      return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Given a list of filenames, 
# we want to rename all the files with 
# the extension hpp # to the extension h 
# by generating a list of tuples of the form (old_name, new_name).

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [(f, f.replace('.hpp','.h')) for f in filenames]

print(filenames)
print(newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

# The permissions of a file in a Linux system are split into three sets of three permissions:
#  read, write, and execute for the owner, group, and others. 
#  Each of the three values can be expressed as an octal number 
#  summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
#  Or it can be written with a string using the letters r, w, and x 
#  or - when the permission is not granted. 
#  For example: 640 is read/write for the owner, read for the group, 
#  and no permissions for the others; converted to a string, 
#  it would be: "rw-r-----" 
#  755 is read/write/execute for the owner, and read/execute for group and others; 
#  converted to a string, it would be: "rwxr-xr-x" 
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
      result = ""
      value_letters = [(4,"r"),(2,"w"),(1,"x")]
      # Iterate over each of the digits in octal
      for digit in [int(n) for n in str(octal)]:
            # Check for each of the permissions values
            for value, letter in value_letters:
                  if digit >= value:
                        result += letter
                        digit -= value
                  else:
                        result += "-"
      return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

# Let's create a function that turns text into pig latin: 
# a simple text transformation that modifies each word 
# moving the first character to the end and appending "ay" 
# to the end. For example, python ends up as ythonpay.

def pig_latin2(text):
      words = [w[1:]+w[0]+"ay" for w in text.split(" ")]
      return " ".join(words)

print(pig_latin2("hello how are you")) # Should be "ellohay owhay reaay ouyay"

def pig_latin3(text):
      return " ".join([w[1:]+w[0]+"ay" for w in text.split(" ")])
print(pig_latin3("hello how are you")) # Should be "ellohay owhay reaay ouyay"


def pig_latin(text):
      # Separate the text into words
      words = []
      for w in text.split(" "):
            # Create the pig latin word and add it to the list
            words.append(w[1:]+w[0]+"ay")
      # Turn the list back into a phrase
      return " ".join(words)


print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

numbers = [23, 32, 45, 0]
# sorted returns a new sorted list
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)

# sort modify the current list
numbers.sort()
print(numbers)

names = ['Mario', 'Luis', 'Alejandro', 'Ale']
#sorted based on other parameter
len_name_sorted = sorted(names, key=len)
print(names)
print(len_name_sorted)