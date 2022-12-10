def greet():
    print("hello world")

greet()
# ans: hello world
# ==================================== 

def add_sub(a,b):
    return a+b,a-b


add,sub=add_sub(7,8)
print(add,sub)
# ans: 15 -1