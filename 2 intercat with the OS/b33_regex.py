"""
Fill in the code to check if the text passed has at
 least 2 groups of alphanumeric characters (including letters,
  numbers, and underscores) separated by one or more whitespace characters.
"""

import re
def check_character_groups(text):
    # \w word with alpahnumeric and underscores
    # \d for matching digits, 
    # \s for matching whitespace characters like space, tab or new line, 
    # \b for word boundaries and a few others.

    result = re.findall(r"\w+\s\w+", text)
    print(result)
    return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

"""
Fill in the code to check if the text passed looks like 
a standard sentence, meaning that it starts with an uppercase letter, 
followed by at least some lowercase letters or a space, 
and ends with a period, question mark, or exclamation point.
"""

import re
def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]+.*[.!?]$", text)
    return result != None

print()
print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("Hello!")) # True
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
print(check_sentence("A2 ad.")) # True

"""
The check_web_address function checks if the text passed 
qualifies as a top-level web address, meaning that it 
contains alphanumeric characters 
(which includes letters, numbers, and underscores), 
as well as periods, dashes, and a plus sign, 
followed by a period and a character-only top-level 
domain such as ".com", ".info", ".edu", etc. 
Fill in the regular expression to do that, 
using escape characters, wildcards, repetition qualifiers, 
beginning and end-of-line characters, and character classes.

"""

import re
def check_web_address(text):
  pattern = r"^.*\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None
print()
print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


"""The check_time function checks for the time format 
of a 12-hour clock, as follows: the hour is between 1 and 12, 
with no leading zero, followed by a colon, 
then minutes between 00 and 59, then an optional space, 
and then AM or PM, in upper or lower case. 
Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?
"""
import re
def check_time(text):
  pattern = r"^([1-9]|^1[012]):([0-5][0-9]) ?(pm|am|PM|AM)$"
  print(text)
  result = re.search(pattern, text)
  result = re.findall(pattern, text)
  print(result)

  return result != None

print()
# print(check_time("20")) # True
# print(check_time("0")) # True
# print(check_time("12")) # True
# print(check_time("10")) # True
# print(check_time("9")) # True

print(check_time("12:45PM")) # True
print(check_time("9:59 am")) # True
print(check_time("9:60 AM")) # false

# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False
