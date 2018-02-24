print range(1, 10)

t1 = ()
l1 = []
d1 = {}

print type(t1)
print type(l1)
print type(d1)

t1 = (1, 2, 3)

t2 = ('1', '3', '5')

print(t1 + t2)

l1 = ['a', ('1', '3', '7')]

l2 = ['1', ('3', '6'), {1: 'a'}]

print(l1 + l2)

l3 = l1 + l2

print l3[0:2]

l3.sort()

print l3

l4 = ['a', 'b', '1', 2, 3]
print (l4)
l4.reverse()

print l3

print l3.remove.__doc__

print(dir(l3))

l4.append('z')

print(l4)

l4.remove('z')

print l4

l4.insert(-1, {1: 'a', 2: 'b'})

print l4

l4.extend(('a', 'b'))

print l4



l4 = ('a', 'b', '1', 2, 3)
print type(l4)


t1 = (1,4,5,2,3,'a','b')

print t1[0]

d2 = dict(enumerate(t1))


t2 = tuple(d2.items())

print t2

a1 = set("abc")
b1 = set("cde")

f = open("C:/Users/Nishant Gupta/Downloads/Backup/Programming/Week 9/HelloWorld.txt")

f.read()

f.read()

print f.mode

print f.name

print f.closed

print f.tell()

f.seek(10)

f = open("C:/Users/Nishant Gupta/Downloads/Backup/Programming/Week 9/HelloWorld.txt")

print f.tell()
print f.read()
print f.tell()

f.seek(-3,2)

print f.tell()

print f.read()

def fun (a=10,b=5,c=11):
    print a
    print b
    print c
    print "addition yeilds : ",
    return a+b+c

print fun()


def fun1(a):

    global y
    y = a
    print y
    b = 20
    print b
fun1(15)
print y

import re as re

m = re.match(r"(..)+","Data")
print m.group(1)

class test:
    x =10
    y = 20

a = test()

print a.x

a.l = 20

print a.l


import re

s1 = "an example word:www!!"

m = re.match('(..)',s1)

print m.groups()

print m.group(1)
