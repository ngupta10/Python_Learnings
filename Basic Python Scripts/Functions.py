"""

Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input

"""

def ex():
    print("Hello World")

ex()

var1 = 5

def ex1(a):
    print(a)

ex1(var1)

""" 

multiple parameter functions: 
1.create 3 variables and assign integer values to them 
2.define a function that prints the difference of 2 parameters 
3.define a function that prints the product of the 3 variables 
4.call the function you made in step 2 using 2 of the variables you made for step 1 
5.call the function you made in step 3 using the 3 variables you created for step 1 

"""

va1 = 1
va2 = 2
va3 = 3

def sub(a,b):
    print(a-b)
def prod(a,b):
    print(a*b)
sub(va2,va1)
prod(va3,va2)

""" 

Calling previously defined functions within functions: 
1.create 3 variables and assign float values to them 
2.create a function that returns the quotient of 2 parameters 
3.create a function that returns the quotient of what is returned by the function from the second step 
and a third  parameter 
4.call the function you made in step 2 using 2 of the variables you created in step 1.  Assign this to a variable. 
5.print the variable you made in step 4 
6.print a call of the function you made in step 3 using the 3 variables you created in step 1 

"""

v1 = 1.2
v2 = 2.6
v3 = 3.9

def quot(a,b):
    return a / b

def quot1(a,b,c):
    return quot(a,b) / c

vare1 = quot(v2,v1)

print(vare1)

print(quot1(v2,v1,v3))