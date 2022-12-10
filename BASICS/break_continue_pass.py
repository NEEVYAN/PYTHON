# for
x=int(input("enter the number of candies : "))
i=1
av=20
while i<=x:
    print(i)
    if i>av:
        print("inufficient candies sorry!")
        break
    i+=1
# ==================================================

# continue 
for i in range(12):
    if i%3==0:
        continue
    else:
        print(i)
# ans:
# 1
# 2
# 4
# 5
# 7
# 8
# 10
# 11
# ==================================================

# pas(it is used to implement empty functions)
for i in range(12):
    if i%3!=0:
        pass
    else:
        print(i)
        
# ans:
# 0
# 3
# 6
# 9