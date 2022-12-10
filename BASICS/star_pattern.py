n=int(input("enter number of rows : "))
i=1
while i<=n:
    j=1
    while j<=n:
        print("*",end=" ")
        j+=1
    print()
    i+=1
# ans :
# enter number of rows : 4
# * * * * 
# * * * *
# * * * *
# * * * *
# ====================================================

n=int(input("enter number of rows : "))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
# enter number of rows : 4
# * 
# * *
# * * *
# * * * *
# ====================================================

n=int(input("enter number of rows : "))
i=n
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=1
# enter number of rows : 4
# * * * * 
# * * *
# * *
# *