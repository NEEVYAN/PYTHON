li=[5,8,9,23]

print(li[3])
23

# print(li[9])
#index out of range
# =============================
for i in li:
    print(i)

# 5
# 8
# 9
# 23
# =============================

# iterators 
it=iter(li)
print(it.__next__())
# 5
print(it.__next__())
# 8
print(it.__next__())
# 9
print(next(it))
# 23

# ===============================
class Top10:
    
    def __init__(self) :
        self.num=1
    
    def __iter__(self):
      return self
        
    def __next__(self):
        
        if self.num<=10:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration
     

value=Top10()

for i in value:
    print(i)
    
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
