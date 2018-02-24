"""

1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]

2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]

"""
print([a for a in range(8,-1,-2)])

print([a**a for a in range(1,5,1)])

print([a*(a-2) for a in range(6,9,1)])

print([a for a in range(2,10,1) if(a !=5)and(a !=6)])

print([a for a in range(10,0,-1) if(a>8)or(a<4)])



