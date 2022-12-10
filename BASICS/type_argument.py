def add(a,b): #(formal arguments)
    print(a+b)

add(6,6) #(actual arguments)
# ans : 12 
# ==================================================

#position
def person(name,age): 
    print("name :",name)
    print("age :",age)

# by changing order 
person(23,"neeraj")
# ans :
# name : 23
# age : neeraj
# which is wrong in order 

# hence 
person(age=23,name="neeraj")
# ans :
# name : neeraj
# age : 23
# ==================================================

# default
def color_fun(color,code=20):
    print("color : ",color)
    print("code : ",code)
    
color_fun("black")
# ans :
# color :  black
# code :  20
# ==================================================

# variable length(when number of parameter that should be passed is not fixed)
def sum(a,*b):
    result=0
    print(a)
    for i in b:
        result=result+i
    print(a+result)
        
  
sum(2,3,4,5)
# ans:
# 14
# ==================================================

