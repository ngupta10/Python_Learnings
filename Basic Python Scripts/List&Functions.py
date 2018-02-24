"""


0.Setup:
 a.create a list of integers and assign it to a variable
 b.create a list of strings and assign it to a variable
 c.create a list of floats and assign it to a variable


1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input


2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input


3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.

4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of
this problem set:  .index(), .append(), .remove(), .insert, or .pop().
Also, make sure that the function prints the resulting list
b.call the function from part
4.a. using one of the lists you made in part 0 of this problem set.

"""

li1 = [1,2,3,4,5]
li2 = ["aaaa","bbbb","ccccc","dddddd","eeeeee"]
li3 = [1.1,2.2,3.3,4.4,5.5]

def ex1(li):
    return li[0]

print(ex1(li1))
print(ex1(li2))
print(ex1(li3))

def ex2(li):
    total =1
    for nums in li:
        total *= nums
    return total
print(ex2(li1))

def ex3(li):
    str =""
    for st in li:
        str += st
    return str
print(ex3(li2))

def ex4(li):
    print(li[2]/li[1])

ex4(li3)

def ex5(li):
    li.append(6)
    li.pop(3)
    li.insert(0,10)
    return li
print(ex5(li1))