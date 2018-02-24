import numpy as np

a = np.array([15,25,14,78,96])

a

print a

# Changing the datatype

a = np.array([15,25,14,78,96], dtype = 'float')

print type(a)

# Creating Sequence of Numbers

a = np.arange(start=0, stop =20)

print a

# Create an Arithmetic Progression

a = np.arange(start =0, stop =20, step=2)

print a

# Reshaping the arrays
a = np.arange(101,113)
print a.reshape(3,4)
print a

## Note that reshape() does not alter the shape of the original array.
# Thus to modify the original array we can use resize( )

a.resize(3,4)

print a

# 2D arrays

g = np.array([[10,20,30],[40,50,60]])

print g

print g.ndim

print g.size

print g.shape


##Creating some usual matrices.
#numpy provides the utility to create some usual matrices which are commonly used for linear algebra.
#To create a matrix of all zeros of 2 rows and 4 columns we can use np.zeros( ):

print np.zeros((2,4),dtype = np.int16)


# To get a matrix of all random numbers from 0 to 1 we write np.empty

print np.empty((2,3))


# To create a matrix of unity we write np.ones( )

print np.ones((3,3))

#To create a diagonal matrix we can write np.diag( )

print np.diag([14,15,16,17])


# To create an identity matrix we can use np.eye( )

print np.eye(5)

# Reshaping 2D arrays
#To get a flattened 1D array we can use ravel( )

g = np.array([[10,20,30],[40,50,60]])

print g
print g.ravel()

# To change the shape of 2D array we can use reshape.
# Writing -1 will calculate the other dimension automatically and does not modify the original array
print g.reshape(3,-1)

print g.shape

# using resize( ) will modify the shape in the original array.

g.resize((3,2))

print g



######
#to get the transpose, trace and inverse we use A.transpose( ) , np.trace( ) and np.linalg.inv( ) respectively

A = np.array([[2,0,1],[4,3,8],[7,6,9]])
b = np.array([1,101,14])
B = np.array([[10,20,30],[40,50,60],[70,80,90]])



print A

print A.transpose()

print np.trace(A)

print np.linalg.inv(A)

# Matrix addition and subtraction can be done in the usual way

print A + B

print A - B

# Matrix multiplication of A and B can be accomplished by A.dot(B). Where A will be the 1st matrix on the left
# hand side and B will be the second matrix on the right side.

print A.dot(B)

# To solve the system of linear equations: Ax = b we use np.linalg.solve( )

print np.linalg.solve(A,b)

# The eigen values and eigen vectors can be calculated using np.linalg.eig( )
# The first row are the various eigen values and the second matrix denotes the matrix of eigen vectors where
# each column is the eigen vector to the corresponding eigen value

print np.linalg.eig(A)


# We can have various trigonometric functions like sin, cosine etc. using numpy:

B = np.array([[0,-20,36],[40,50,1]])
print np.sin(B)

# In order to get the exponents we use **

print B**2

print B > 25

# np.absolute, np.sqrt and np.exp return the matrices of absolute numbers, square roots and exponentials respectively.

print np.absolute(B)

#print np.sqrt(B)

print np.exp(B)

# To find the sum, minimum, maximum, mean, standard deviation and variance respectively we use the following commands

A = np.arange(1,10).reshape(3,3)

print A.sum()
print A.min()
print A.max()
print A.mean()
print A.std()   #Standard deviation
print A.var()  #Variance


# to obtain the index of the minimum and maximum elements we use argmin( ) and argmax( ) respectively.

print A.argmin()

print A.argmax()

# If we wish to find the above statistics for each row or column then we need to specify the axis

print A.sum(axis=0)
print A.mean(axis = 0)
print A.std(axis = 0)
print A.argmin(axis = 0)

# By defining axis = 0, calculations will move in downward direction i.e. it will give the statistics for each column.
#To find the min and index of maximum element fow each row, we need to move in rightwise direction so we write axis = 1:

print A.min(axis =1)
print A.max(axis=1)

#To find the cumulative sum along each row we use cumsum( )

print A.cumsum(axis=1)



#######

# Creating 3D arrays

X = np.array( [[[  1, 2,3],
                [ 4, 5, 6]],
               [[7,8,9],
                [10,11,12]]])

print X.shape

print X.ndim

print X.size

print X

print "\n"

# axis = 0 returns the sum of the corresponding elements of each 2D array.
# axis = 1 returns the sum of elements in each column in each matrix while axis = 2
# returns the sum of each row in each matrix.
print X.sum(axis = 0)
print X.sum(axis = 1)
print X.sum(axis = 2)

#Indexing in arrays

x = np.arange(0,10)

print x[2]

print x[2:5]

#If we want to change the value of all the elements from starting upto index 7,
# excluding 7, with a step of 3 as 123 we write:

x[:7:3] = 123

print x

#To reverse a given array we write:

x = np.arange(10)

print x

print x[::-1]

#Consider 3D array

X = np.array( [[[  1, 2,3],
                [ 4, 5, 6]],
               [[7,8,9],
                [10,11,12]]])


#To extract the 2nd matrix
print X[1,:,:]


#To extract the first element from all the rows we write
print X[:,:,0]

