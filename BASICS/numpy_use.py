from numpy import *
# ====================================

num=array([1,2,3,4,5,6])
print(num)
# ans : [1 2 3 4 5 6]

# ======================================
# for 2d array numpy must be installed 
# 5 ways of making an array 
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()
# ========================================================

num=array([1,2,3,4,5.6,6.7])
print(num)
# ans :  [1.  2.  3.  4.  5.6 6.7](all converted to float)
# ========================================================

num=linspace(0,13,14)
# starts from 0
# ends at 13
# breaks 0 to 13 in 14 equal parts 
print(num)
# ans : [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13.] 

num=linspace(0,13,5)
# starts from 0
# ends at 13
# breaks 0 to 13 in 5 equal parts 
print(num)
# ans : [ 0.    3.25  6.5   9.75 13.  ] 

# if parts is not mentioned it breaks the starts and end in 50 equal parts 

# ===========================================================

num = arange(1,15,1)
# works same as range(start,end,increment)
print(num)

# ans : [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14] 
# ===========================================================

num = zeros(5)
num2= zeros(5,int)
print(num)
print(num2)
# ans:
# [0. 0. 0. 0. 0.]
# [0 0 0 0 0]
# ===========================================================

num = ones(5)
num2= ones(5,int)
print(num)
print(num2)
# ans:
# [1. 1. 1. 1. 1.]
# [1 1 1 1 1]