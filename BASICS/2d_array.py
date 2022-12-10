from numpy import *

num=array([
         [2,3,4,5],
         [7,8,9,0]
         ])
print(num)

# ans:
# [[2 3 4 5]
#  [7 8 9 0]]

print(num.dtype)
print(num.ndim)
print(num.shape)
print(num.size)

# ans :
# int32
# 2 (dimension)
# (2, 4)(rows,columns)
# 8 (total elements)

# ========================================

# multiply dimension to 1 dimeension 

num2=num.flatten()
print(num2)
# ans : [2 3 4 5 7 8 9 0]

#to change order of array from

num3=num.reshape(4,2) # 2 rows 2 columns
print(num3)
# ans :
# [[2 3]
#  [4 5]
#  [7 8]
#  [9 0]]