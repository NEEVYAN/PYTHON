def count(li):
    even=0
    odd=0
    for i in li:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd



li=[2,3,4,5,6,7,8,9]
even,odd=count(li)
print("even : ",even)
print("odd : ",odd)

# or 
print("even : {} odd : {}".format(even,odd))

# even :  4
# odd :  4
# even : 4 odd : 4
# ======================================================

def display(li):
    even=[]
    odd=[]
    for i in li:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return even,odd
li=[2,3,4,5,6,7,8,9]
even,odd=display(li)
print("even : ",even)
print("odd : ",odd)

# or 
print("even : {} odd : {}".format(even,odd))

# even :  [2, 4, 6, 8]
# odd :  [3, 5, 7, 9]
# even : [2, 4, 6, 8] odd : [3, 5, 7, 9]