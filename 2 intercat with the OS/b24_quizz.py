#!/usr/bin/env python3
import csv
"""
We also need to pass a dialect as a parameter to
 this function. There isn't a well-defined standard 
 for comma-separated value files, so the parser needs 
 to be flexible. Flexibility here means that there are 
 many parameters to control how csv parses or writes data.
  Rather than passing each of these parameters to the reader 
  and writer separately, we group them together 
  conveniently 
  into a dialect object.

Dialect classes can be registered by name so that callers 
of the CSV module don't need to know the parameter 
settings in advance. We will now register a dialect 
empDialect.

"""

def read_employees(csv_file_location):
    
    # Read the rows of the file into a dictionary
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

path = '/home/student-01-1674e84f360d/data/employees.csv'
path = 'employees.csv'
employee_list = read_employees(path)
# print(employee_list)

def process_data(employee_list):
    # initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list

    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    # We now have to remove the redundancy and return a dictionary. We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)
print(dictionary)

def write_report(dic, report_file):
    with open(report_file, "w+") as f:
        for dep in sorted(dic):
            line = '{dep}:{n}\n'.format(dep=dep, n=dic[dep])
            l = str(dep)+':'+str(dic[dep])+'\n'
            print(line)
            print(l)
            f.write(l)
        f.close()

def write_report(dic, report_file):
    with open(report_file, "w+") as f:
        for dep, employe_count in sorted(dic.items()):
            line = '{dep}:{n}\n'.format(dep=dep, n=employe_count)
            f.write(line)
        f.close()

path = '/home/student-01-1674e84f360d/data/report.txt'
path = 'report.txt'
write_report(dictionary, path)