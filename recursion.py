#1.Simple one
'''
def hello(x):
    if x == 0:
        return
    else:
        print("This is recursion")
        hello(x-1)
        
hello(10)
'''
#2.Factorial

def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)
z = sum(5)
print(z)