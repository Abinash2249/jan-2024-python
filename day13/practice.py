# Positional argument, default and keyword argument, arbitrary argument

def addition(*args):
    return(sum(args))

print(addition(1,2,3))
print(addition(0,2,10))


def subtraction(**kwargs):
    return(kwargs["b"]-kwargs["a"])

print(subtraction(a=1,b=2))
print(subtraction(a=1,b=2,c=3))
print(subtraction(a=1,b=2,c=3,d=4))
print(subtraction(a=1,b=2,c=3,d=4,e=5))


def addition(a,b,c,d,e,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(args)
    print(kwargs)

addition(1,2,3,4,5,6,7,8,9,10,name="John")


def is_even_number(num):
    return num % 2 == 0

num = int(input("Enter a number: "))
result = is_even_number(num)
print(result)





