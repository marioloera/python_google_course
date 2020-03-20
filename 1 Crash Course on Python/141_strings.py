
def double_word(word):
    return word*2+str(len(word))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

x = '323.98'
print(x.isnumeric())

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system XD")) # Should be: OS

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    print('1:'+input_string)
    new_string = input_string.replace(' ','')
    print('2:'+new_string)
    reverse_string = new_string[::-1]
    print('3:'+reverse_string)
    return new_string.lower() == reverse_string.lower()

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for l in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
        if l != ' ':
            new_string = new_string + l
            reverse_string = l + reverse_string
    return new_string.lower() == reverse_string.lower()

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def convert_distance(miles):
    km = miles * 1.6 
    result = "{miles:} miles equals {km:.1f} km".format(miles=miles, km=km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

