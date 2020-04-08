class Computer:
    def __init__(self):
        self.name = "Yasin"
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
# c1.age = 32
if c1.compare(c2):
    print("Same Age")
else:
    print("Different Age")