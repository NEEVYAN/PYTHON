a=int(input("Enter the number you wanna search : "))
li=[2,7,9,4,5,8]
pos=0
for i in li:
    if a==i:
        print("YES NUMBER AT INDEX ",pos)
        break
    else:
        pos+=1
else :
    print("NOT FOUND")
        