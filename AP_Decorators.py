# # Decorators
# def hello():
#     print('Hello')
#
#
# greet = hello
# del hello
# print(greet)  # But greet still pointing on memory location of function hello, so it is works
#
#
# # print(hello)  # Error
#
# # Decorators can works because of ability of function to act like variables
# # Decorators - supercharge our functions
#
# # HOC, Higher Order Function; Examples:
# def greet(func):
#     func()
#
#
# def greet2():
#     def func():
#         return 5
#     return func
#
#
# # Decorators 2
# # Decorator Pattern
def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')

    return wrap_function
#
#
# @my_decorator
# def hello(greeting='Hi ', greeting2="sss"):
#     print(greeting, greeting2)
#
#
# @my_decorator
# def bye():
#     print('See ya later')
#
# # *******
# # Hellooo
# # *******
# hello('Hello')
# # *******
# # See ya later
# # *******
# bye()
#
# # What we do upper:
# my_decorator(hello)()  # It is a true background of my_decorator

# Performance decorator
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result

    return wrapper
#
#
# @performance
# def long_time():
#     for i in range(10 ** 5):
#         pass
#
#
# long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper


@my_decorator
@authenticated
@performance
def message_friends(user):
    for i in range(10 ** 8):
        pass
    print('message has been sent')
    for i in range(10 ** 8):
        pass


message_friends(user1)
