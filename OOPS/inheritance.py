# Single level inheritance 
class A:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
a=A()
a.feature1()
a.feature2()
# feature 1 working
# feature 2 working

class B(A):
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")
        
b=B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()
# feature 1 working
# feature 2 working
# feature 3 working
# feature 4 working
# ================================================================

# Multi level inheritance 
# A class 
# B(A) class 
class C(B):
    def feature5(self):
        print("feature 5 is working")

c=C()
c.feature1()
c.feature5()
# feature 1 working
# feature 5 is working