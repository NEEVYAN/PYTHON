a=10
b=34
c="neeraj"
d=3.234
# ==================================
print(id(a),id(b))
#print addresses

print(a+b)
print("a :",a,"b :",b)

print(id(c))
# ===================================
# address concept in variable 
x=3
y=x
print(id(x))
print(id(y))
print(id(3))
# ans:
# 140723941397352
# 140723941397352
# 140723941397352
# all have same address
# ======================================

print(type(a),type(c),type(d))
# ans : <class 'int'> <class 'str'> <class 'float'>