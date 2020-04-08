from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print ("Hello")
            sleep(1) # Not to collide with below class

class Hi(Thread):   #Include Thread to run both classes/methods in multi threading
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)  #Still Collision is happening, add sleep between two objects
t2.start()

t1.join()
t2.join()
print ("Bye") # Bye will print before both the objects execution completion, so we have to tell the main thread to wait so add above join functios