"""

Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
1.create a 3 key: value pair dictionary and assign it to a variable
2.access and print a value from the list in step 1 by key
3.add a fourth key: value pair to the dictionary from step 1
4.print the dictionary from step 3
5.print the length of the dictionary from step 3

"""

dict = {1: 11, 2:"Nishant", 3:"Gupta"}

print(dict[1])

dict[30] = "Food"

print(dict)

print(len(dict))

""" 

Reassignment by Key and Del: 
1.create a 2 key: value pair dictionary and assign it to a variable 
2.print the dictionary from step 1 
3.reassign a key from the dictionary in step 1 a different value than its original value 
4.print the dictionary from step 3 
5.remove a key: value pair from the dictionary from step 3 using del 
6.print the new dictionary 

"""

di = {1:"Nishant",2:"Harrogate Court"}

print(di)

di[2] = "Gupta"

print(di)

del di[1]

print(di)