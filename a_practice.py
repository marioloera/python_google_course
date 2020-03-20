numbers = [3, 5, 7]
print(numbers)
number_x2 = [2*n for n in numbers]
print(number_x2)


number_a = [n for n in numbers]
print(number_a)

sum_numbers = sum(numbers)
print(sum_numbers)

num_dic ={'a':3, 'b':5, 'c':7}
print(num_dic)

sum_numbers = sum([n for n in num_dic.values()])
print(sum_numbers)

def print_(x):
    print('print ' + str(x))
    return True

x=1
while(x!=0):
    x = int(input('enter x:'))
    if x==1:
        print('first part')
        continue
    
    if x==2 and print_(x):
        print('second part')
        continue
    print('afer continue')


print('...............')
import sys

x = sys.argv[1]
print(x)