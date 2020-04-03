
# The "toc" dictionary represents the table of contents for a book. 
# Fill in the blanks to do the following: 


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# 1) Add an entry for Epilogue on page 39. 
toc["Epilogue"] = 39

# 2) Change the page number for Chapter 3 to 24. 
toc["Chapter 3"] = 24

# 3) Display the new dictionary contents. 
print(toc)

# 4) Display True if there is Chapter 5, False if there isn't.
print("Chapter 5" in toc)

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for name, feature in cool_beasts.items():
    print("{} have {}".format(name, feature))

def count_letter(text):
      result = {}
      for l in text:
            if l not in result:
                  result[l] = 1
            else:
                  result[l] += 1
      return result

t ='aaaaabbbcc'
c = count_letter(t)
print(c)
print(c['a'])

import collections
c = collections.Counter(t*1)
print(c)
print(c['a'])

# In Python, a dictionary can only hold a single value for a given key. 
# To workaround this, our single value can be a list containing multiple values. 
# Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
# Fill in the blanks to print a line for each item of clothing with each color, 
# for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe.keys():
      for color in wardrobe[item]:
	      print("{} {}".format(color, item))

# The email_list function receives a dictionary,
#  which contains domain names as keys, and a list of users as values. 
#  Fill in the blanks to generate a list that contains complete email addresses 
#  (e.g. diana.prince@gmail.com).

def email_list(domains):
      emails = []
      for domain in domains.keys():
            for user in domains[domain]:
                  email = '{user}@{domain}'.format(user=user, domain=domain)
                  emails.append(email)
      return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# The groups_per_user function receives a dictionary, 
# which contains group names with the list of users. 
# Users can belong to multiple groups. 
# Fill in the blanks to return a dictionary 
# with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
      user_groups = {}
      # user_groups = {'userA':['group1', 'group2']}
      # Go through group_dictionary
      for group in group_dictionary.keys():
            # Now go through the users in the group
            for user in group_dictionary[group]:
                  if user not in user_groups:
                        user_groups[user] = []
                  user_groups[user].append(group)
      return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		            "public":  ["admin", "userB"],
		            "administrator": ["admin"] }))