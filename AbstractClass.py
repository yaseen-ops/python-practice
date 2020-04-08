from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print('It is running')

class WhiteBoard(Computer):

    def process(self):
        print('It is Writing')

class Programmer:

    def code(self,com):
        print('Solving Bugs')
        com.process()

#com = Computer()
com1 = Laptop()
#com.process()
#com1.process()
com2 = WhiteBoard()
prog = Programmer()
prog.code(com2)