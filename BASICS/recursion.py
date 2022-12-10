# BY DEFAULT IN PYTHON RECURSION LIMIT IS 1000 TIMES BUT WE CAN INCREASE OR DECRESE IT 
# ======================================================================================

import sys 
print(sys.getrecursionlimit())
# 1000 

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# 2000 

def fac(n):
    if n==0:
        return 1
    else :
        return n*fac(n-1)

print(fac(6))
# 720
