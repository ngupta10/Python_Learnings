"""

and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator

"""

ex1 = True and True
ex2 = True and False
ex3 = True or True
ex4 = False or False
ex5 = not False
ex6 = not True

print(ex1,ex2,ex3,ex4,ex5,ex6)


""" 

order of operations for Boolean operators: 
1.make var1 evaluate to False by changing or removing a single Boolean operator 
2.make var2 evaluate to True by changing or removing a single Boolean operator """


var1 = not 3 > 1 
print(var1)
