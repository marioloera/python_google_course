import re

"""
Fill in the code to check if the text passed contains 
the vowels a, e and i, 
with exactly one occurrence of any other character in between
"""
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

print()
"""
Fill in the code to check if the text passed contains punctuation symbols: 
commas, periods, colons, semicolons, question marks, and exclamation points.
"""
def check_punctuation (text):
  result = re.search(r"[,.:;!?]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't patternular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

"""
Fill in the code to check if the text passed includes a possible 
U.S. zip code, formatted as follows: exactly 5 digits, and sometimes,
 but not always, followed by a dash with 4 more digits. 
 The zip code needs to be preceded by at least one space,
  and cannot be at the start of the text.

"""
print()
import re

def create_exp(text):
    zipformats =[r"\d{5}", r"\d{5}[-]\d{4}"]
    zip_ending = r"[ ,\.]"
    pattern = ""
    for zipformat in zipformats:
        if pattern != "":
            pattern += '|'
        fullzipformat = ' {zf}{ze}| {zf}$'.format(zf=zipformat, ze=zip_ending)

        print(fullzipformat)
        pattern += fullzipformat

    print(pattern)
    result = re.findall(pattern, text)

    print(text)
    print(result)

    # formated 
    for r in result:
        x = re.sub(zip_ending, "", r)
        print("\tformated:<{x}>".format(x=x))

    return pattern

def check_zip_code(text,formatype):
    #result = re.search(r" \d\d\d\d\d^[\d]| \d\d\d\d\d-\d\d\d\d", text)

    result = re.findall(r" \d\d\d\d\d[ \.,]", text)
    result = re.findall(r" \d\d\d\d\d$", text)
    result = re.findall(r" \d\d\d\d\d[ \.,]| \d\d\d\d\d$", text)

    result = re.findall(r" \d{5}[ \.,]", text)
    result = re.findall(r" \d{5}$", text)
    result = re.findall(r" \d{5}[ \.,]| \d{5}$", text)

    #using formats
    zipformats =[r" \d{5}", r"\d{5}-\d{4}"]
    #print(zipformats)
    zip_ending = r"[ ,\.]"


    pattern = zipformats[formatype]+zip_ending +'|' + zipformats[formatype]+'$'

    print(pattern)
    result = re.findall(pattern, text)

    print(text)
    print(result)

    # formated 
    for r in result:
        x = re.sub(r"[ \.,]", "", r)
        x = re.sub(zip_ending, "", r)
        print("\tformated: {x}".format(x=x))
    return result != None

# (check_zip_code("90210 is a TV show 1234 123456")) # False
# (check_zip_code("The zip codes for New York are 85258-0001, 12345-1234 and 10001, 10002 thru 11104")) # True
# (check_zip_code("90210 is a TV show 85258x1234")) # False
# (check_zip_code("90210 is a TV show 85258-0001-1234")) # False
# (check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001")) # True
# (check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False



text = "The zip codes for 123456 1234 12345x1234 New York are 85258-0001, 12345-1234 and 10001, 10002 thru 11104" # True

check_zip_code(text, 0)
check_zip_code(text, 1)
print('_'*30)
create_exp(text)