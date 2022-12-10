# some list properties
# list values can be changed means ut is muttable in nature

# .append()
# .insert()
# .remove()
# .pop()
# del
# min
# max
# sum
# sort

tup=[34,45,67,34,56,67]

print(tup)
# ans : [34,45,67,34,56,67]

print(tup[2:]) 
# ans :67,34,56,67

print(tup[-1])
# ans : 67

tup.append(41)
print(tup)
# ans : [34, 45, 67, 34, 56, 67, 41]

tup.insert(2,54)
# insert at position 2 number 54
print(tup)
# ans : [34, 45, 54, 67, 34, 56, 67, 41]

tup.remove(45)
# remove number 45
print(tup)
# ans : 34, 54, 67, 34, 56, 67, 41]

tup.pop(3)
# remove number at index 3
print(tup)
# ans : [34, 54, 67, 56, 67, 41]

del tup[2:]
# delete everything after index 2
print(tup)
# ans : [34, 54]

tup=[23,34,54,54,26,78,12,89,57]

tup.sort()
print(tup)
# ans: [12, 23, 26, 34, 54, 54, 57, 78, 89]

print(max(tup))
# ans : 89

print(min(tup))
# ans : 12

print(sum(tup))
# ans : 427


# ==================================

# tup2=["neeraj","aryan","anand"]

# print(tup2)
# # ans : ['neeraj', 'aryan', 'anand']

# # ==================================
# tup3=["neeraj",9.03,67]

# print(tup3)
# # ans : ["neeraj",9.03,67]

# # ====================================
# tup4=[tup,tup2]

# print(tup4)







