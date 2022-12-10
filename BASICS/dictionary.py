dictionary={11:"aaaa",22:"bbbb",33:"cccc",44:"dddd"}
print(dictionary[22])
print(dictionary[44])
print(dictionary[33])
print(dictionary[11])
# ans:
# bbbb
# dddd
# cccc
# aaaa

# ===========================================================================
print(dictionary.get(11,"not found"))
# ans : aaaa 
print(dictionary.get(12,"not found"))
# ans : not found (12 is not in dictionary)
# ===========================================================================

# two list in dictionary 
name=["neeraj","abhay","raja","karan"]
lang=["python","js","cpp","ruby"]
dictionary2=dict(zip(name,lang))
print(dictionary2)
# ans : {'neeraj': 'python', 'abhay': 'js', 'raja': 'cpp', 'karan': 'ruby'}
# ===========================================================================

dictionary2["shubham"]="html"
# adding new value to dictionary 
print(dictionary2)
# ans : {'neeraj': 'python', 'abhay': 'js', 'raja': 'cpp', 'karan': 'ruby', 'shubham': 'html'}
# ===========================================================================

del dictionary2["raja"]
print(dictionary2)
# ans : {'neeraj': 'python', 'abhay': 'js', 'karan': 'ruby', 'shubham': 'html'}
# ===========================================================================

prog={"JS":"ATOM","CS":"VS","PYTHON":["PYCHARM","SUBLIME"],"JAVA":{"JSE":"NETBEANS","JEE":"ECLIPSE"}}
print(prog["JS"])
print(prog["PYTHON"])
print(prog["PYTHON"][0])
print(prog["JAVA"])
print(prog["JAVA"]["JEE"])
# ans :
# ATOM
# ['PYCHARM', 'SUBLIME']
# PYCHARM
# {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}
# ECLIPSE

print(prog.keys())
print(prog.values())
# ans:
# dict_keys(['JS', 'CS', 'PYTHON', 'JAVA'])
# dict_values(['ATOM', 'VS', ['PYCHARM', 'SUBLIME'], {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}])


