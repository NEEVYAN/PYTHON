# first way 

a=0
b=1
n=int(input("enter the num : "))
if n==1:
    print(a,end=" ")
elif n==2:
    print(a,end=" ")
    print(b,end=" ")
else :
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

# enter the num : 5
# 0 1 1 2 3
# ========================================= 
 
# factorial 
def fac(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
n=fac(6)
print(n)

# 720   
        
        