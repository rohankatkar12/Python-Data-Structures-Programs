#Write a decorator for division function. When Divisor is zero then it should'n be divide.

def deco(func):
    def inner_func(a,b):
        if b==0:
            return "Divisor should not be zero"
        else: 
            return func(a,b)
    return inner_func


def div(a,b):
    return(a/b)

obj = deco(div)
print(obj(10,20))