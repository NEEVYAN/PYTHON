from numpy import *

arr1=array([1,2,3,4,5])
arr1=arr1+5
print(arr1)
# ans :[ 6  7  8  9 10] 
# ==========================================================

arr2=array([6,7,8,9,10])
arr3=arr1+arr2
print(arr3)
# ans : [12 14 16 18 20]
# ==========================================================

# vectorised operation 
# sin()
# cos()
# sqrt()
# log()
# sum()
# min()
# max()
# sort()
# concatenate(1,2)

print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(concatenate([arr1,arr2]))

# ans :
# [-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
# [ 0.96017029  0.75390225 -0.14550003 -0.91113026 -0.83907153]
# [1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
# [2.44948974 2.64575131 2.82842712 3.         3.16227766]
# 40
# 6
# 10
# [ 6  7  8  9 10]
# [ 6  7  8  9 10  6  7  8  9 10]
# ==========================================================

# copy of array

# first way 
x=array([1,3,5,7,9])
y=x
print(x,id(x))
print(y,id(y))
# ans : 
# [1 3 5 7 9] 1806374301552
# [1 3 5 7 9] 1806374301552
# address is same
# ==========================================================

# second way 
x=array([1,3,5,7,9])
y=x.view()
print(x,id(x))
print(y,id(y))
# ans : 
# [1 3 5 7 9] 1531459300944
# [1 3 5 7 9] 1531459301424

# address is different but changes in x leads to change in y 
x[4]=78
print(x,id(x))
print(y,id(y))
# ans : 
# [ 1  3  5  7 78] 2995334705104
# [ 1  3  5  7 78] 2995334705392
# ==========================================================

# third way 
x=array([1,3,5,7,9])
y=x.copy()
x[4]=78
print(x,id(x))
print(y,id(y))

# ans :
# [ 1  3  5  7 78] 2289388318672
# [1 3 5 7 9] 2289388318960