a=5
print(type(a)) #int

b=3.4
print(type(b)) #float

c=2+4j
print(type(c)) #complex

d=int(b)
print(d) #3

e=float(a)
print(e) #5.0

f=complex(a,b)
print(f) #5+3.4j

g=b<a
print(g)
print(type(b))
#true
#float

print(int(True)) #1
print(int(False)) #0


# ===============================================
h=[34,45,56,67,78,89]
print(type(h))

i=(34,45,56,67,78,89)
print(type(i))

j={34,45,56,67,78,89}
print(type(j))

k={34:23,45:32,56:23,67:89,78:54}
print(type(k))

# ans:
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'dict'>
# ===============================================

name="suraj"
print(type(name)) #str

# ================================================
print(list(range(10)))
# ans : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2,20,2)))
#start from 2
#end at < 20
#add 2 to every number
# ans : [2, 4, 6, 8, 10, 12, 14, 16, 18]