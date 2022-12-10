class student:
    
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        self.lap=self.Laptop()
        
    def info(self):
        print(self.name,self.branch)
        self.lap.show()
    # ===========================================
    
    # Inner class 
    class Laptop:
        
        def __init__(self):
            self.ram="16b"
            self.name="HP"
            self.warranty=1
        def show(self):
            print(self.ram,self.name,self.warranty)

s1=student("neeraj","Btech")
s2=student("Akanksha","Bdes")

s1.info()
s2.info()
# neeraj Btech
# 16b HP 1
# Akanksha Bdes
# 16b HP 1



# lap1=student.Laptop()
# lap1.show()
# 16b HP 1