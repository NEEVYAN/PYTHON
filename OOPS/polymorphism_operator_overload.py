a=5
b=8
# for add 

# this is general 
print(a+b)
# but in real this is called  
print(int.__add__(a,b))

# 13
# 13
# similarly for:
    # int.__sub__()
    # int.__mul__()
    # also called magic methods 
# ===============================================

a='7'   
b="8"
print(a+b)  #78
print(str.__add__(a,b)) #78
# =================================================

# operator overloading concept 

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,second):
        # m1=self.m1+second.m1
        # or 
        m1=int.__add__(self.m1,second.m1)
        # m2=self.m2+second.m2 
        # or 
        m2=int.__add__(self.m2,second.m2)
        # c=student(m1,m2)
        s3=student(m1,m2)
        return s3
    
    def __gt__(self,second):    #greater than
        # here int.__add__(self.m1,self.m2) = self.m1 + self.m2 
        # here int.__add__(other.m1,other.m2) = other.m1 + other.m2
        if int.__add__(self.m1,self.m2)>int.__add__(second.m1,second.m2):
            return 1
        else :
            return 0
        
s1=student(78,89)
s2=student(39,90)
s3=s1+s2  #it will automatically calls __add__(s1,s2) method
print(s3.m1,s3.m2,s3.m1+s3.m2)
# 117 179 296

if s1>s2:   
    print("s1 wins")
else :      
    print("s2 wins")
        
        