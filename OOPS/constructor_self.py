class computer :
    pass
comp1=computer()
comp2=computer()

print(id(comp1))
print(id(comp2))

# 1368677212944
# 1368677213008
# ===============================================

class employee:
    def __init__(self):
        self.name="neeraj"
        self.age=23  
    def update(self):
        self.name="mukesh"
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
        
    
e1=employee()
e2=employee()

print(e1.name," ",e1.age)
print(e2.name," ",e2.age)
# neeraj   23
# neeraj   23


e1.name="suraj"
e1.age=27
print(e1.name," ",e1.age)
print(e2.name," ",e2.age)
# suraj   27
# neeraj   23

e1.update() #here self call itself as e1
print(e1.name," ",e1.age)
# mukesh   27

a=e1.compare(e2)
print(a)
# False 