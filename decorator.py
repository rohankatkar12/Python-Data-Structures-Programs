#1. Write a decorator for division function. When Divisor is zero then it should'n be divide.

# def deco(func):
#     def inner_func(a,b):
#         if b==0:
#             return "Divisor should not be zero"
#         else: 
#             return func(a,b)
#     return inner_func


# def div(a,b):
#     return(a/b)

# obj = deco(div)
# print(obj(10,20))






# #2. Multiple Decorators

# def deco1(fun):
#     def wrapper_func():
#         print("Hii")
#         return fun()
#     return wrapper_func
    
# def deco2(fun):
#     def wrapper_func():
#         print("whatsapp")
#         return fun()
#     return wrapper_func

# def deco3(fun):
#     def wrapper_func():
#         print("How Are You")
#         return fun()
#     return wrapper_func

# @deco1
# @deco2
# @deco3
# def show():
#     print("Rohan")
    
# show()



# 3. Decorator for E-Commerce product offer price
# Decorate to offer for limited period of time
import datetime

def decorator():
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(12, 13) #11:58 am
    end_time = datetime.time(12, 14) #12:00 pm
    
    def prod_deco(fun):
        def inner_deco(product, price):
            if current_time < start_time or end_time <= current_time:
                return fun(product, price)
            
            if start_time<= current_time <= end_time:
                today_price = (price*40)/100
                print(product)
                print(f"Price :{price} Rupees")
                print('Flat 40% Off')
                print(f"Today Price :{today_price} Rupees")
        
        return inner_deco
    return prod_deco


@decorator()
def func(product, price):
    print(product)
    print(f"Price :{price} Rupees")
    
obj = func("APPLE iPhone 14 (Blue, 128 GB)", 67999)


# obj = decorator()
# obj1 = obj(func)
# res = obj1("APPLE iPhone 14 (Blue, 128 GB)", 67999)
