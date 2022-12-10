class hello:
    def run(self):
        for i in range(5):
            print("hello")

class hii:
    def run(self):
        for i in range(5):
            print("hii")  
        
a=hello()
b=hii()

a.run()
b.run()

# one execution after another 
# hello
# hello
# hello
# hello
# hello
# hii
# hii
# hii
# hii
# hii
# ================================================

# threading concept 
from threading import *

class hello2(Thread):
    def run(self):
        for i in range(5):
            print("hello2")

class hii2(Thread):
    def run(self):
        for i in range(5):
            print("hii2")  
        
a=hello2() #thraed1
b=hii2()   #thread2

a.start() #start automatically checks the run method in class
b.start()

print("byee")  #main thread

# MIXED OUTPUT NOT PARALLEL OUTPUT 
# hello2
# hello2 byee
# hello2
# hii2
# hii2
# hello2
# hello2
# hii2
# hii2
# hii2
# ======================================================

from threading import *
from time import sleep

class hello3(Thread):
    def run(self):
        for i in range(5):
            print("hello3")
            sleep(1)

class hii3(Thread):
    def run(self):
        for i in range(5):
            print("hii3")  
            sleep(1)
        
a=hello3()
sleep(.2)
b=hii3()

a.start() 
b.start()

a.join() #it will check wheather all hello3 is printed
b.join() #it will check wheather all hii3 is printed

print("byee")

# PARALLEL OUTPUT 
# hello3
# hii3
# hello3
# hii3
# hello3
# hii3
# hello3
# hii3
# hello3
# hii3
# byee