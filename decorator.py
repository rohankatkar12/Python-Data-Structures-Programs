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






#Multiple Decorators

def deco1(fun):
    def wrapper_func():
        print("Hii")
        return fun()
    return wrapper_func
    
def deco2(fun):
    def wrapper_func():
        print("whatsapp")
        return fun()
    return wrapper_func

def deco3(fun):
    def wrapper_func():
        print("How Are You")
        return fun()
    return wrapper_func

@deco1
@deco2
@deco3
def show():
    print("Rohan")
    
show()



