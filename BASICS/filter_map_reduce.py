def iseven(n):
    even=[]
    for i in n:
        if i%2==0:
            even.append(i)
    return even

num=[2,3,4,5,6,7,8,9,10]
a=iseven(num)
print(a)
# [2, 4, 6, 8, 10]
# ============================================================

# filter 
num=[2,3,4,5,6,7,8,9,10]

even=list(filter(lambda n:n%2==0,num))
print(even)
# [2, 4, 6, 8, 10]
# ==========================================================

# map 
even = [2, 4, 6, 8, 10]
double = list(map(lambda n : n+2,even))
print(double)
# [4, 6, 8, 10, 12]

# ==========================================================
from functools import reduce

num=[2,3,4,5,6,7,8,9,10]
sum = reduce(lambda a,b : a+b ,num)
print(sum)
# 54