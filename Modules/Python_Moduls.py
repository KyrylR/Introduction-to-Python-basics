# from Modules.utility import divide, multiply, Student    # or we can use * instead of divide, multiply
# from Shopping.shopping_cart import buy
#
#
# stud1 = Student()
# print(type(stud1))  # <class 'Modules.utility.Student'>
#
# if __name__ == '__main__':
#     print(__name__)     # __main__
#     print(divide(2, 2))  # 1.0
#     print(multiply(2, 2))  # 4
#     print(buy({3, 2, 1}))  # [{1, 2, 3}]

# from random import choice, shuffle, random
#
# print(random())  # random number
# print(choice([1, 2, 3, 4]))  # choice a random item in a sequence
#
# my_list = [1, 2, 3, 4, 5, 6]
# shuffle(my_list)
# print(my_list)  # shuffle our list

# # Random game where you need to guess a number
# import sys
# from random import randint
# from time import time
#
#
# def performance(func):
#     def wrapper(*args, **kwargs):
#         time1 = time()
#         result = func(*args, **kwargs)
#         time2 = time()
#         print(f'Your game took: {time2 - time1}')
#
#     return wrapper
#
#
# first_num = sys.argv[1]  # 0 index for name of file
# second_num = sys.argv[2]
#
#
# @performance
# def randomgame():
#     try:
#         print(f'Guess a number between {first_num} and {second_num}')
#         random_num = randint(int(first_num), int(second_num))
#         while True:
#             try:
#                 guess_num = int(input('Guess a number: '))
#                 if guess_num == random_num:
#                     print('You are genius!')
#                     break
#                 elif guess_num > random_num:
#                     print('It is a little bit higher')
#                 else:
#                     print('It is lower')
#             except ValueError:
#                 print('Please Enter a number next time')
#     except ValueError:
#         print('Please Enter a number next time')
#     else:
#         print('Thanks for the game ;) See ya)))')
#
#
# randomgame()

# Useful modules
from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 4, 5, 3]
# print(Counter(li))  # Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1})
#
# sentence = 'abc ds wea'
# print(Counter(sentence))  # Counter({'a': 2, ' ': 2, 'b': 1, 'c': 1, 'd': 1, 's': 1, 'w': 1, 'e': 1})
#
# dictionary = defaultdict(lambda: 10, {'a': 1, 'b': 2})
# print(dictionary['c'])  # 10

# d = {'c': 100}
# d['a'] = 1
# d['b'] = 2
#
# d2 = {'c': 100}
# d2['b'] = 2
# d2['a'] = 1
#
# print(d.items() == d2.items())  # True, but:
# print(d.items())  # dict_items([('c', 100), ('a', 1), ('b', 2)])
# print(d2.items())   # dict_items([('c', 100), ('b', 2), ('a', 1)])

# import datetime
#
# print(datetime.time(5, 45, 2))  # 05:45:02
# print(datetime.date.today())    # 2021-07-15
#
# from array import array
# import sys
#
# arr = array('i', [i for i in range(1, 10 ** 5)])
# li = [i for i in range(1, 10 ** 5)]
# print(sys.getsizeof(arr))  # 400060
# print(sys.getsizeof(li))  # 800984
