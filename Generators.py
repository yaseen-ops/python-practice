"""def topten():
    yield 4   #It is a generator

val = topten()
#print (val)
print (val.__next__()) #Yield returns in the format of Iterator
"""
"""
def topten():
    yield 1    #Yield will not breaks the method as 'return' does that.
    yield 2
    yield 3

val = topten()

for i in val:
    print(i)
"""
class Test:

 def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

#val = topten()
val = Test.topten()
for i in val:
    print(i)