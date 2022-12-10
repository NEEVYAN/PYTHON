from numpy import *
# ==============================================
m=matrix("1,2,3,4 ; 5,6,7,8")
print(m)
# ans :
# [[1 2 3 4] 
#  [5 6 7 8]]   

n=matrix("1,2,3 ; 4,6,9 ; 9,3,2")
print(n)
# [[1 2 3]
#  [4 6 9]
#  [9 3 2]]

print(diagonal(n))
#print digonal of n
# [1 6 2]

print(n.min())
print(n.max())
# 1
# 9
# ===============================================

