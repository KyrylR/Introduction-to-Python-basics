# # Generators
# # we never create a list in memory if use
# # generator like this
# print((range(0, 100)))
# # instead of when we use memory, like this:
# print(list(range(0, 100)))
#
#
# def make_list(num):  # what we do here: list(range(num))
#     result = []
#     for item in range(num):
#         result.append(item)
#     return result
#
#
# print(make_list(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# range(10)  # is generator and it's iterable
# list(range(100))  # a list created from generator and it's iterable, but not a generator
#
# # if obj has a dander method __iter__ it'll be an iterable obj
# # also generator is a subset of an iterable

# # Create our own generator:
# def generator_function(num):
#     for it in range(num):
#         # yield says, just pause the function, just yield i
#         # give i and when you tell me to keep going again, then i'll keep going
#         yield it*2
#
#
# try:
#     g = generator_function(3)
#     print(next(g))  # 0
#     print(next(g))  # 2
#     print(next(g))  # 4
#     print(next(g))  # 6
# except StopIteration as err:
#     print('StopIteration Error')

# for i in generator_function(10):
#     print(f'{i}')
#     if i > 5:
#         break


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


# @performance
# def long_time():
#     print('1')
#     for i in range(10 ** 8):
#         pass
#
#
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10 ** 8)):
#         pass
#
#
# long_time()  # It took 1.4162635803222656 s
# long_time2()  # It took 3.464097261428833 s

# # Create our own for loop:
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             # print(iterator)
#             # print(next(iterator))
#             next(iterator)
#         except StopIteration:
#             print('StopIteration')
#             break
#         except Exception as err:
#             print(err)
#
#
# special_for([1, 2, 3])  # we can see that the obj still in the same position of memory
#
#
# # Create our own range
# class MyGen(object):
#     current = 0
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration
#
#
# @performance
# def own_types():
#     gen = MyGen(0, 10 ** 8)
#     for i in gen:
#         pass
#
#
# @performance
# def build_in_types():
#     gen = range(0, 10 ** 8)
#     for i in gen:
#         pass
#
#
# print('Own type')
# own_types()  # It took 28.199716329574585 s
# print('Build in type')
# build_in_types()  # It took 1.8361592292785645 s

# # Create our own fibonacci range
# class MyFibonacciGen(object):
#     current = 0
#     next = 1
#     state = 0
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyFibonacciGen.state <= self.last:
#             MyFibonacciGen.state += 1
#             result = MyFibonacciGen.current
#             temp = MyFibonacciGen.next
#             MyFibonacciGen.next += MyFibonacciGen.current
#             MyFibonacciGen.current = temp
#             return result
#         raise StopIteration
#
#
# @performance
# def own_types():
#     gen = MyFibonacciGen(0, 10 ** 3)
#     for i in gen:
#         pass
#
#
# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#
#
# @performance
# def Andr_types():
#     for x in fib(10 ** 3):
#         pass
#
#
# print('Own type')
# # It took 718.6488845348358 s for 10^7
# own_types()  # It took 7.056485652923584 s for 10^6
# print('Andr type')
# # It took 692.5728919506073 s for 10^7
# Andr_types()  # 6.633790731430054 s for 10^6
