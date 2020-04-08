class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):    #Operational Overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        #return self.m1, self.m2
        return '{} {} '.format(self.m1, self.m2)

s1 = Student(56,65)
s2 = Student(96,54)
s3 = s1 + s2   # Integer, string knows what + operator does, but class doesn't know, so we have to define it. (method __add__)
#print (s3.m2)
if s1 > s2:
    print ('S1 wins')
else:
    print ('S2 wins')

#print (s1.__str__()) #call __str__ method and gives you the output what if i want to give only s1.
print(s1)
print(s2)