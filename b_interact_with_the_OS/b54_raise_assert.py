

def validate_user(username, minlen):
    # assert may be removed form the execution during optimizer
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise   ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False

    if not username.isalnum():
        return False

    return True


print(validate_user("dasd", 2)) # True
print(validate_user("dasd", 20)) # False
print(validate_user("da# ssd", 2)) # False
# print(validate_user(["dasd"], 10)) # assert
# print(validate_user("dasd", 10)) # value error



def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

my_list = [27, 5, 9, 6, 8]
print(RemoveValue(27))
# print(RemoveValue(27)) # value error

my_word_list = ['east', 'after', 'up', 'over', 'inside']
def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    #     if type(item) is not str:
    #         raise TypeError("Word list must be a list of strings")
    myList.sort()
    return myList

print(OrganizeList(my_word_list))
my_new_list = [6, 3, 8, "12", 42]
# print(OrganizeList(my_new_list)) # AssertionError:

# Revised Guess() function
import random
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:   
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except:
        return None

participants = ['Jack','Jill','Larry','Tom']
print(Guess(participants))

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))