from math import floor

def sorting(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]>li[j]:
                temp=li[i]
                li[i]=li[j]
                li[j]=temp
    return li

def search(a,n):
    max=len(a)-1
    min=0
    for i in range(len(a)):
        mid=floor((max+min)/2)
        if(a[mid]==n):
            return True
        elif(a[mid]>n):
            max=mid
        elif(a[mid]<n):
            min=mid
        
li=[1,5,9,2,4,3,56,76,54]
n=int(input("enter the bumber to be searched : "))
a=sorting(li)
print(a)

if search(a,n):
    print("FOUND")
else :
    print("NOT FOUND")