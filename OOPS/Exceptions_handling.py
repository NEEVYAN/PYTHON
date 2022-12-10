# SyntaxError (compile Time Error) forgot to use colon
# logical error 2+3=4(wrong logic)
# Run time Error 2/0 
# ===========================================================
a=8
b=5
c=0

try:
    print("process started")
    print(a/b)
    
except Exception as e:
    print("your problem is ",e)
    
finally:
    print("process end")
    
# process started
# 1.6
# process end
# ==========================================================


a=8
c=0

try:
    print("process started")
    print(a/c)
    
except Exception as e:
    print("your problem is ",e)
    
finally:
    print("process end")
    
# process started
# your problem is  division by zero
# process end