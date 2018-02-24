import numpy as np

##Indexing with Arrays of Indices

x = np.arange(11,35,2)
print x

i = np.array([0,1,5,3,7,9])

print x[i]

##similar manner we create a 2D array j of indices to subset x.

j = np.array( [ [ 0, 1], [ 6, 2 ] ] )
print x[j]

##Similarly we can create both  i and j as 2D arrays of indices for x

x = np.arange(15).reshape(3,-1)

print x

i = np.array([[0,1],[2,0]])
j = np.array([[1,1],[2,0]])

## i and j must be of same shape
print x[i,j]

#To extract ith index from 3rd column we write

print x[i,2]

#For each row if we want to find the jth index we write

print x
print x[:,j]


#use indexing with arrays to assign the values
x = np.arange(10)
x
x[[4,5,8,1,2]] = 0
print x

#When the list of indices contains repetitions then it assigns the last value to that index

x = np.arange(10)
x
x[[4,4,2,3]] = [100,200,300,400]
print x

##Notice that for the 5th element(i.e. 4th index) the value assigned is 200, not 100.
#Caution: If one is using += operator on repeated indices then it carries out the operator only once on repeated indices.

x = np.arange(10)
x[[1,1,1,7,7]]+=1
print x


###Indexing with Boolean Arrays


#We create a 2D array and store our condition in b. If we the condition is true it results in True otherwise False

a = np.arange(12).reshape(3,4)
b = a > 4
print b

print a[b]

#Now 'a' becomes a 1D array with the selected elements
#This property can be very useful in assignments

a[b] = 0
print a

x = np.arange(15).reshape(3,5)
y = np.array([True,True,False])             # first dim selection
z = np.array([True,True,False,True,False])       # second dim selection

print x[y,:]

print x[:,z]


#Stacking various arrays
A = np.array([[10,20,30],[40,50,60]])
B = np.array([[100,200,300],[400,500,600]])

#To join them vertically we use np.vstack( )

print np.vstack((A,B))

#To join them horizontally we use np.hstack()

print np.hstack((A,B))

#newaxis  helps in transforming a 1D row vector to a 1D column vector.

from numpy import newaxis
a = np.array([4.,1.])
b = np.array([2.,8.])
print a[:,newaxis]

#Splitting the arrays

z = np.arange(1,16)

#Using np.hsplit( ) one can split the arrays
print np.hsplit(z,5)

#On passing 2 elements, It splits 'z' after the third and the fifth element.

print np.hsplit(z,(3,5))



##For 2D arrays np.hsplit( ) works as follows

A = np.arange(1,31).reshape(3,10)
print A
print np.hsplit(A,5)   # Split a into 5 arrays

##In the above command A gets split into 5 arrays of same shape.
#To split after the third and the fifth column we write:

print np.hsplit(A,(3,5))

##Copying

x = np.arange(1,16)
#We assign y as x and then say 'y is x'

y = x
print y is x

y.resize(3,5)

print x.shape


#Creating a view of the data

z = x.view()
print z is x

z.resize(5,3)

print z.shape


##Changing an element in z

z[0,0] = 1234

## values in x also gets alter

print x

##Creating a copy of the data

z = x.copy()

print z is x

#Changing the values in z does not make any alterations in x

z[0,0] = 9999

print x


