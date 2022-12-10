def div(a,b):
    if a<b:
        a,b=b,a
    return a/b

print(div(4,2))
print(div(2,4))
# 2.0
# 2.0

# ==========================================================

# decorators
def division(a,b):
    return a/b

def smart_div(num):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return num(a,b)
    return inner

div=smart_div(division)
print(div(4,8))
# 2.0 