a ,b=5,4

# ====================================
#first way
c=a
a=b
b=c
print(a,b)

# ====================================
# second way
a=a+b
b=a-b
a=a-b
print(a,b)

# ====================================
# third way
a=a^b
b=a^b
a=a^b
print(a,b)

# ====================================
# fouth way
a,b=b,a    #two_root concept of python
print(a,b)
