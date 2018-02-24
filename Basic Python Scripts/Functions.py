# 2. Write a recursive function to compute x raised to the power of n.

def recursive_power(x, y):
    if y ==1:
        return x
    else:
        return x * recursive_power(x, y-1)

try:
    base = int(raw_input("Please enter the base number : "))
    pow_base = int(raw_input("Please enter the power to which %i to be raised : "%base))
    print ("The result is : %i"%(recursive_power(base, pow_base)))
except ValueError:
    print ("You entered Invalid value")


#Sort the list using lambda function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#  Sort the list by second item 1 and 0.

mylist = [["john", 1, "a"], ["larry", 0, "b"]]

def getKey(item):
    return item[1]

#print (sorted(mylist, key = getKey))

print (sorted(mylist, key=lambda mylist:mylist[1]))


#Sort the list using operator.itemgetter function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
# Sort the list by second item 1 and 0.

import operator

mylist = [["john", 1, "a"], ["larry", 0, "b"]]

print(sorted(mylist, key=operator.itemgetter(1)))