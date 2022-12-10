def person(name,*data):
    print(name)
    print(data)

person("neeraj",34,"suraj",45)

# ans :
# neeraj
# (34, 'suraj', 45)
# ===================================================

# but if we wanna specify all the values 
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person("neeraj",age=34,brother="suraj",age2=45)

# ans :
# neeraj
# {'age': 34, 'brother': 'suraj', 'age2': 45}
# age 34
# brother suraj
# age2 45