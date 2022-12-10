from array import *
# ====================================================== 

# creation of array 
arr=array("i",[])
length=int(input("enter the length of array : "))
# input 
for i in range(length):
    x=int(input("enter the data : "))
    arr.append(x)
    
#print
print(arr)
# =========================================================

# finding index of element in array 
num=int(input("enter the number you wanna find : "))

for i in range(length):
    if arr[i]==num:
        print(i)
        break
else:
    print("not found")