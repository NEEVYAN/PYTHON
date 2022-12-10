# # Single level inheritance 
# class A:
    
#     def __init__(self):
#         print("init of A")
        
#     def feature1(self):
#         print("feature 1 working")
        
#     def feature2(self):
#         print("feature 2 working")

# class B(A):
    
#     def __init__(self):
#         print("init of B")
        
#     def feature3(self):
#         print("feature 3 working")
        
#     def feature4(self):
#         print("feature 4 working")

# class C(A):
    
#     def __init__(self):
#         super().__init__()
#         print("init of C")
        
#     def feature5(self):
#         print("feature 5 working")
        
# a=A()
# # init of A

# b=B()
# # init of B

# c=C()
# # it will call both constructor of A and C 
# # init of A
# # init of C
# ==================================================

class D:
    def __init__(self) :
        print("D constructor")
    def show(self):
        print("show a message D")

class E:
    def __init__(self) :
        print("E constructor")
    def show(self):
        print("show a message E")
        
class F(D,E):
    def __init__(self) :
        super().__init__()
        print("F constructor")
        
f=F()
# METHOD RESOLUTION ORDER 
# check which is called first 
# D constructor
# F constructor

f.show()
# show a message D