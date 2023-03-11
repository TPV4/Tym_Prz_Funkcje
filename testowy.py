import sys

def clear(var):
    var=lambda:sys('cls')
    return var

a=[1,2,3]
a=clear(a)
print(a)