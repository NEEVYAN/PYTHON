class student:
    
    name="neeraj"
    
    # ==================================
    #instance method
    def __init__(self,m1,m2,m3) :
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
      
    #accessors(get the value)
    def get(self):
        return self.m1
    
    # mutators(sets the value)
    def set(self,value):
        self.m1=value
    # ===================================
    
    #class method
    @classmethod
    def info(cls):
        cls.name="suraj" #it changes the name of student class
        print(cls.name)
        
    # ===================================
    
    # static method 
    @staticmethod
    def idc():
        print("i dont want self or cls ")
      
s1=student(23,45,67)
s2=student(54,67,26)

print(s1.avg())
print(s2.avg())
# 45.0
# 49.0

print(s1.get())
print(s2.get())
# 23
# 54

student.info()
student.idc()
# suraj
# i dont want self or cls
