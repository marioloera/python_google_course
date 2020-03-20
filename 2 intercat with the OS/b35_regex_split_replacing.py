"""The convert_phone_number function checks for a U.S. 
phone number format: XXX-XXX-XXXX 
(3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
Fill in the regular expression to complete this function.
"""

import re
def convert_phone_number(phone):
    regex = r"\b(\d{3})-(\d{3})-(\d{4})\b"
    # r = re.findall(regex, phone)
    # print(r)
    # r = re.search(regex, phone)
    # print(r)
    newformat = r"(\1) \2-\3"
    result = re.sub(regex, newformat, phone)
    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

"""
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. 
The phone number field contains U.S. phone numbers, 
and needs to be modified to the international format, 
with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, 
to use the transform_record function to do that.
"""
print()
import re
def transform_record(record):
    regex = r"(\d{3}-\d{3}-?\d{4})"
    # r = re.findall(regex, phone)
    # print(r)
    # r = re.search(regex, phone)
    # print(r)
    newformat = r"+1-\1"

    new_record = re.sub(regex, newformat, record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


print()
"""The multi_vowel_words function returns all words with 
3 or more consecutive vowels (a, e, i, o, u). 
Fill in the regular expression to do that.
"""

import re
def multi_vowel_words(text):
  pattern = r"\w+[aeiou]{3}\w+"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']
print(multi_vowel_words("Hello world!")) 
# []
