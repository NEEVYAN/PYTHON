# r = read 
# w = write 
# a = append
# rb = read binary 
# wb = write binary 
# =====================READ===============================

f=open('FILEHANDLING1','r')
# print(f.read())
# My name is xyz 
# i am from xyz
# i wanna be a in future
# this file gonna by read by the python file handler
# this is jst a simple program
# this is fr only illustration purpose only
# =========================================================
print(f.readline())
# My name is xyz (only first line)

print(f.readline())
# My name is xyz 

# i am from xyz

# =====================WRITE===============================

f2=open("FILEHANDLING2","w") 
#it will check if you have a file if not it will make one
f2.write("hey this is new file")       #----------------> 1
f2.write("i will be added to the same file") #----------> 2

# output: new file with all the contents in same line 
# if 1 or 2 any data will be deleted the output don't have the data

# =====================APPEND===============================

f3=open("FILEHANDLING3","a") 
#it will check if you have a file if not it will make one
f3.write("hey this is appended file")   #----------------> 1
f3.write("i will be append to the same file") #----------> 2

# output: new file with all the contents in same line 
# if 1 or 2 any data will be deleted then also the output have the data

# =====================READ BINARY, WRITE===============================
# it will print the code of any image 
f4=open("mountain.jpg","rb")
f5=open("mountain2.jpg","wb")

for i in f4:
    f5.write(i)
    
# create a new copy of image name as mountain2