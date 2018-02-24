"""
1.Correct the program given below:

total = raw_input('What is the total amount for your online shopping?')
country = raw_input('Shipping within the US or Canada?')
if country == "US":
    if total <= "50":
        print "Shipping Costs $6.00"
    elif total <= "100":
            print "Shipping Costs $9.00"
    elif total <= "150":
            print "Shipping Costs $12.00"
    else:
        print "FREE"
if country == "Canada":
    if total <= "50":
        print "Shipping Costs $8.00"
    elif total <= "100":
        print "Shipping Costs $12.00"
    elif total <= "150":
        print "Shipping Costs $15.00"
    else:
        print "FREE"




"""


total = input('What is the total amount for your online shopping?')
country = raw_input('Shipping within the US or Canada?')
if country == "US":
    if total <= 50:
        print "Shipping Costs $6.00"
    elif total <= 100:
            print "Shipping Costs $9.00"
    elif total <= 150:
            print "Shipping Costs $12.00"
    else:
        print "FREE"
if country == "Canada":
    if total <= 50:
        print "Shipping Costs $8.00"
    elif total <= 100:
        print "Shipping Costs $12.00"
    elif total <= 150:
        print "Shipping Costs $15.00"
    else:
        print "FREE"



#2.Write a program that uses raw_input to prompt a user for their name and then welcomes them.
#     Example: Enter your name:"yourName"
#                  Hello "yourName"

name = raw_input("Enter you name : ")
print ("Hello \"%s\""%(name))


# Write a program which prompts the user for a Fahrenheit temperature, convert the temperature to
# Celsius and print out the converted temperature.

tem = input("Enter the temperature in fahrenheit : ")
print ("The temperature you entered is : %i F"%(tem))

tem_cel = float((tem-32.0)*0.5556)

print ("The equivalent Celsius to the temperature %.2f F enetered is : %.2f C"%(tem,round(tem_cel,2)))


# Write a program to prompt the user for hours and rate per hour to compute gross pay.
#      Example: Enter Hours: 35
#                  Enter Rate: 2.75
#                  Pay: 96.25

hours = input("Enter Hours : ")
rate = input("Enter Rate : ")
pay = hours*rate
print ("For %.2f hours and a pay rate of %.2f , the Gross Pay is : %.2f"%(hours,rate,pay))



#Write a for loop that prints all elements of a list and their position in the list.
#       a = [4,7,3,2,5,9]

a =[4,7,3,2,5,9]

for i in a:
    print ("The Element at index position %i is : %i"%(a.index(i),i))


#. Write a program which should create a dictionary of key:values.
#       'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]

dict = {i : chr(64+i) for i in range(1,27)}
print dict


# . Write a program to reverse/inverse key:value like below.
#     dict1 = { 'a': 1, 'b':2 }
#      Expected result : dict2 = { 1: 'a', 2: 'b' }

dict1 = { 'a': 1, 'b':2 }
dict2 = {v: k for k, v in dict1.iteritems()}
print dict2


# Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
# Expected result {'a': 1, 'c': 3, 'b': 2, 'd': 4} [Hint: Use Enumerate function]

L = ['a', 'b', 'c', 'd']

my_dict = dict(enumerate(L))

print my_dict
