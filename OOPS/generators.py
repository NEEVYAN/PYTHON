def topten():
    n=1
    while n<=10:
        yield n*n
        n+=1
        
a=topten()      
for i in a:
    print(i)
     
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100 