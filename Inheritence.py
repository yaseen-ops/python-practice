"""class A:
    def feature1(self):
        print ("feature 1 is printed")
    def feature2(self):
        print ("feature 2 is printed")

#class B:    ##Output 1
class B(A):  ## Output 2    B becomes the child/sub class of A which is called inheritence
    def feature3(self):
        print ("feature 3 is printed")
    def feature4(self):
        print ("feature 4 is printed")


a1 = A()
b1 = B()
c1 = C()
a1.feature1()
b1.feature1()
"""
# Output 1:  # here class A and class B are different classes, we cannot access methods of A from B. So we have set class B as child of class A
"""$ python inheritence.py
feature 1 is printed
Traceback (most recent call last):
  File "inheritence.py", line 17, in <module>
    b1.feature1()
AttributeError: 'B' object has no attribute 'feature1'
"""

# Output 2 :
"""$ python inheritence.py
feature 1 is printed
feature 1 is printed"""


class A:
    def feature1(self):
        print("feature 1 is printed")

    def feature2(self):
        print("feature 2 is printed")


# class B:    ##Output 1
class B(A):  ## Output 2
    def feature3(self):
        print("feature 3 is printed")

    def feature4(self):
        print("feature 4 is printed")


# Adding class C after Output 2
class C(B):
    def feature5(self):
        print("feature 5 is printed")


c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()

# Output 3:
"""$ python inheritence.py
feature 1 is printed
feature 3 is printed
feature 5 is printed
"""

# Class B is a single inheritence, Class C is multiple inheritence