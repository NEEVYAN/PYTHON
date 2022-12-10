class calculator:
    
    def add(self,a,b):
        return a+b
    
c1=calculator()
print(c1.add(4,5))
# 9

# but what about c1.add(4,5,6)(three arguments) definately it will show error 
# hence we can go for :
# =============================================================================
#Method overloading(means more parameters are passed than required )
class calculator2:
    
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None :
            return a+b
        else :
            return a
            
    
c2=calculator2()
print(c2.add(4,5,6))
print(c2.add(4,5))
print(c2.add(4))
# 15
# 9
# 4
# =============================================================================

# overriding 
class father:
    
    def car(self):
        print("ferrari")
        
class son_previous(father):
        pass

class son_after(father):
    
    def car(self): #same method of father hence this will override the father method
        print("Rolls Royals")
    
class A(son_after):
        pass

s1=son_previous()
s1.car()
# ferrari

s2=son_after()
s2.car()
# Rolls Royals

a=A()
a.car()
# Rolls Royals