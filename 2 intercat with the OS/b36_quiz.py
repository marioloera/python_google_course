"""
Here, you will find a file named script.py. 
The aim of this script is to use regex to find all 
instances of the old domain ("abc.edu") 
in the user_emails.csv file and then 
replace them with the new domain ("xyz.edu").
"""
# /home/student-01-2c45110b7bbb/
#!/usr/bin/env python3

#Import libraries
import re
import csv
import time


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
        in the domain position, false if not."""
    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
        the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main1():
    """Processes the list of emails, replacing any instances of the
        old domain with the new domain."""
    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'
    csv_file_location = 'user_emails.csv'
    #csv_file_location = '/home/student-01-2c45110b7bbb/data/' + csv_file_location
    report_file = 'updated_user_emails.csv'
    #report_file = '/home/student-01-2c45110b7bbb/data/' + report_file
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        f.close()

    for email in user_email_list:
        if contains_domain(email, old_domain):
            old_domain_email_list.append(email)
            replaced_email = replace_domain(email, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
        
        for old_email, new_email in zip(old_domain_email_list, new_domain_email_list):
            #print('\t<{}> -> <{}>'.format(old_email, new_email))
            if user[email_index] == ' ' + old_email:
                user[email_index] = ' ' + new_email

        #print(str(user) + '\t' + str(email_index))
    

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


def main2():
    """Processes the list of emails, replacing any instances of the
        old domain with the new domain.
    """

    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'
    csv_file_location = 'user_emails.csv'
    report_file = 'updated_user_emails.csv'
    user_data_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        f.close()

    for user in user_data_list[1:]:
        name, email = user
        email = replace_domain(email, old_domain, new_domain)
        #print('\t<{}>'.format(email))
        user[1] = email

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()

t1 = time.time()
for x in range(10):
    main2()
t2 = time.time()
p1 = t2-t1
print(p1)
