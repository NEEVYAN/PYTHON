
# to check the concept of printing of a 
a=10

def fun():
    a=5
    print("In a : ",a)
    
fun()
print("out a : ",a)

# In a :  5
# out a :  10
# =================================================

# if we want to access the same a everywhere 
a=10 

def fun():
    print("In a : ",a)
    
fun()
print("out a : ",a)


# In a :  10
# out a :  10
# =================================================

# if we want to change the whole a 
a=10 

def fun():
    global a
    a=26
    print("In a : ",a)
    
fun()
print("out a : ",a)


# In a :  26
# out a :  26
# =================================================

# if we want to change the outer a but not inner a 
a=10 

def fun():
    a=26
    x=globals()["a"]
    print("In a : ",a)
    globals()["a"]=19
    
fun()
print("out a : ",a)


# In a :  26
# out a :  19