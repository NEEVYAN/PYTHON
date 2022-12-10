# ABC=abstract Base Class 

class computer:
    
    def open(self):
        # print("plug in")
        pass 
    
comp=computer()
comp.open()
# Nothing got print
# ==========================================

from abc import ABC,abstractmethod
class computer2(ABC):
    
    @abstractmethod
    def open(self):
        # print("plug in")
        pass

class laptop(computer2) :
    
    def open(self):
        print("hey this is abstract method print")

lap=laptop()
lap.open()