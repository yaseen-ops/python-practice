class A:
    def __init__(self):
        print("Class A in init")

    def feature1(self):
        print('feature 1A is printed')

    def feature2(self):
        print("feature 2 is printed")


class B:
    def __init__(self):
        print("Class B in init")
        super().__init__()  # To Access the Parent class construction(Init method) but this super() we can access any methods

    def feature1(self):
        print("feature 1B is printed")

    def feature4(self):
        print("feature 4 is printed")


class C(A, B):
    def __init__(self):
        print("Class C in init")
        super().__init__()  # It prints A first as by MRO (Method Resolution Order )
    def feat(self):
        super().feature2() #We can call any super class methods by using "super()"


#a1 = A()
# b1 = B()
c1 = C()
c1.feature1() # though both A & B classes have feature1 methods, it will call Class A per MRO
c1.feat()