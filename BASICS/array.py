from array import * 
# first visit the table 
# ==================================================

vals=array("i",[2,5,6,7,8,9])
print(vals)
# ans : array('i', [2, 5, 6, 7, 8, 9])
# ==================================================

vals=array("i",[2,5,6,-7,8,9])
print(vals)
# ans : array('i', [2, 5, 6, -7, 8, 9])
# ==================================================

# vals=array("i",[2,5,4.5,7,8,9])
# print(vals)
# ans : 'float' object cannot be interpreted as an integer because of i
# ==================================================

vals=array("i",[2,5,4,7,8,9])
print(vals.buffer_info())
# ans: (2464204635152, 6) (address,size)
# ==================================================

vals=array("i",[2,5,4,7,8,9])
vals.reverse()
print(vals)
# ans:array('i', [9, 8, 7, 4, 5, 2])

# ==================================================
vals=array("i",[2,5,4,7,8,9])
for i in vals:
    print(i)

# OR 

for i in range(len(vals)):
    print(vals[i])
    
    
# ans :
# 2
# 5
# 4
# 7
# 8
# 9
# =================================================

arr=array(vals.typecode,(a for a in vals)) 
# changes in first "a" will make data different

for e in arr:
    print(e)
# ans:
# 2
# 5
# 4
# 7
# 8
# 9