"""class A:
    def show(self):
        print('print show in Class A')

class B(A):
    pass

Obj = B()  #As Class B inherites Class A, it will call method show in Class A.
Obj.show()
"""
class A:
    def show(self):
        print('print show in Class A')

class B(A):
    def show(self):      #Now the same method added in Class B, it will call it from B first and runs it - this is called method overriding
        print('print show in Class B')

Obj = B()
Obj.show()