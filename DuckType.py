class Pycharm:
    def execute(self):
        print('Running')
        print('Compiling')

class MyIde:
    def execute(self):
        print("Debug")
        print('Running')
        print('Compiling')

class Laptop:
        def code(self,ide):
            ide.execute()

ide = MyIde()
lap1 = Laptop()
lap1.code(ide)
