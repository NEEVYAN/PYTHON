# INSTANCE VARIABLES ARE DECLARED INSIDE INIT METHOD WHOSE VALUES CAN BE DIFFERENT FOR 
# DIFFERENT OBJETS BUT CLASS VARIABLE IS SAME FOR ALL OBJECTS 
# ====================================================================================

class branch:
    student="neeraj" #class variables
    def __init__(self):
        self.name="cse" #instance variables 
        self.number=21

b1=branch()
b2=branch()

b1.name="IT"
b2.number=23

print(b1.name," ",b1.number," ",b1.student)
print(b2.name," ",b2.number," ",b2.student)
# IT   21   neeraj
# cse   23   neeraj
# ===================================================

# TO CHANGE CLASS VARIABLE 
branch.student="suraj"
print(b1.student)
print(b2.student)
# suraj
# suraj

