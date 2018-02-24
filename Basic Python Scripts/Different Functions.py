# coding=utf-8
# Authored by Nishant Gupta


# Checking Range

#range is memory intensive
print range(10)

#xrange is not memory intensive

for i in xrange(10,20,2):
    print i


t1 =()
l1=[]
d1={}

print type(t1)
print type(l1)
print type(d1)

l1=["a","b"]
l2=[1,2]

l3 = l1+l2

print l3

l4 = [("apple","ball","cat"),("dog","lion","tiger")]
print type(l4)

print l4[1]

print dir(l3)
l3 = ['a','b',1,2]
print(type(l3))

print(sorted(l3, reverse=False))
print(sorted(l3, reverse=True))

l3.insert(2,'z')

l3.insert(-1,'y')

print l4

print l3


a = [1,2,3]
b=[2,5,8]

a.extend(b)

print a

print l3.count('a')

l3.append(l4)

print l3

t1 = ('apple','ball','cat')
print type(t1)

l5 = list(t1)
print type(l5)

print l1*4

t2 = tuple(l3)
print type(t2)

t1 = (1)
t2 = (2)
print cmp(t1,t2)

t1 = ('apple')
t2 = ('ball')

print cmp(t1,t2)

t1 = ('apple','ball')
t2 = ('apple','ball','cat')

print cmp(t1,t2)
print cmp(t2,t1)
enumerate(t2)
print tuple(enumerate(t2))

d = {'a':'apple','b':'ball','c':'cat'}

print d['a']

print d.items()

l = d.items()

print type(l)

print l

print tuple(d.iteritems())

print d.keys()

print d.values()

print d.pop('c')

print dir(d)

d.update({'c':'cat'})

d.popitem()

print(d.get('b'))


