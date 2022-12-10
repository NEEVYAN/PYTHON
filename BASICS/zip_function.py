li1=["x","y","z"]
li2=[2,3,4]

new=dict(zip(li1,li2))
print(new)
# {'x': 2, 'y': 3, 'z': 4}
# ==========================================

new2=list(zip(li1,li2))
print(new2)
# [('x', 2), ('y', 3), ('z', 4)]
# ==========================================

new3=set(zip(li1,li2))
print(new3)
# {('x', 2), ('z', 4), ('y', 3)}
# ==========================================

new4=zip(li1,li2)

for (a,b) in new4:
    print(a,b)
# x 2
# y 3
# z 4