class colour: 
    
    def __init__(self): #like constructor in cpp and java
        print("white")
    
    
    def colorname(self): 
        print("black")


# we don't require to call __init__ as it is like constructor 
# hence it will automatically printed  
     
c1=colour() 
c1.colorname() 
# white
# black

# ==============================================

class device:
    def __init__(self,name,ram):
        self.name=name
        self.ram=ram
    def display(self):
        print("device is : ",self.name,self.ram)

comp1=device("dell",16)
comp2=device("hp",18)
comp1.display()
comp2.display()

# device is :  dell 16
# device is :  hp 18


        
        


        


        
        
        
       