# integer
 
x=int(input("enter 1st num : "))
y=int(input("enter 1st num : "))
print(x+y)

# ==================================================================================

#charcater

ch=input("enter the string but will print only one alphabet : ")[0]
print(ch)

ch=input("enter the string but will print only one alphabet : ")
print(ch[0])

# ==================================================================================

#evaluation
from math import ceil
result=ceil(eval(input("enter expression and i will evaluate : ")))
print(result)

# ans:
# enter expression and i will evaluate : 2+34/45
# 3
# ==================================================================================

#argv
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
print(x+y)
# ans:
# PS C:\Users\LICAGENCY\Desktop\python> python user_input.py 4 9
# 13