"""Fix the regular expression used in the rearrange_name
 function so that it can match middle names, 
 middle initials, as well as double surnames.
"""
import re
def rearrange_name(name): 
    pattern = r"^(.*), (.*)$" # mario
    pattern = r"^(\w*), (\w*)$" # original
    pattern = r"^([\w \.-]*), ([\w \.-]*)$"

    result = re.search(pattern, name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Loera, Mario"))
print(rearrange_name("Kennedy, John F."))

"""
The long_words function returns all words that are at least 7 characters. 
Fill in the regular expression to complete this function.
"""
import re
def long_words(text):
    pattern = r"\b[a-zA-Z1-9_]{7}\b"
    pattern = r"[a-zA-Z1-9_]{7}"
    pattern = r"\b[\w]{7}\b" # for exactly 7, and to cut the word include \b
    pattern = r"[\w]{7,}" # at least, no need to  include \b
    #pattern = r"\b[\w]{7,}\b"
    result = re.findall(pattern, text)
    return result
print(long_words("1234567                            ")) # ['morning']
print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never abcd_67. drink tea! late at night.")) # []

"""
Add to the regular expression used in the extract_pid function,
 to return the uppercase message in parenthesis, after the process id.
"""
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2] )

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

