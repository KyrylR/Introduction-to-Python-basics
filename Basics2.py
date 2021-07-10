# # Conditional logic
#
# is_old = False
# is_licenced = True
#
# if is_old & is_licenced:  # id ... elif ... else structure
#     print('Car')
#     print("Helllloooo")
# # elif condition: ...
# else:
#     print('WooooW')
#
# print('Car') if is_old else print('Car2')  # Ternary operators
# condition_if_True if condition else condition_if_False

# All false values:
# None, False, 0, 0.0, 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
#   obj.__bool__() returns False
#   obj.__len__() returns 0

# Example:
# if bool(None) | bool('') | bool():
#     print("Lol")
# else:
#     print("It's ok")  # It's ok

# # Short Circuiting
# is_Friend = True
# is_User = None
# # is_User after or will be ignored because of short Circuiting,
# # also it is logical :)
# if is_Friend or is_User:
#     print("User is funny")
#

# # Logical operators: >, >=, <, <=, ==, !=, and, or, not, &, |
# if not (True & False):
#     print(ord('A'))  # 65
#     print(ord('a'))  # 97
#
# is_magician = False
# is_expert = True
#
# if is_magician and is_expert:
#     print('1')
# elif is_magician and not is_expert:
#     print('2')         # we wanna know if you are not magician,
# elif not is_magician:  # it's easier to read code when we use this, instead
#     print('3')         # of else

# # is vs ==, when 'is' checks location in memory, '==' just compare items
# print(1 == True)  # True by bits
# print('' == False)  # False
# print([] == 1)  # False
# print(10 == 10.0)  # True
# print([3, 2] == [2, 3])  # True
# print(ord('1'))  # 49
#
# a = [1, 2, 3]
# b = a
# print(a is b)  # True


# # Loops
# # Data structure
# # must be iterable; Ex: str, [], (), {} and ect.
# # iterated(action) -> one by one check each
# # item in the collection.
# for item in {1, 2, 3}:
#     for x in ['a', 'b']:
#         print(item, x)
# print(item, x)  # It's still exist

# # Loops for Dictionaries
# users = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }
#
# for k, v in users.items():
#     print(f'Key: {k} and value: {v}')  # prints elements of dict users.
#

# # Simple func -> int(sum elements in list), int(quantity elements in list)
# my_list = [1, 2, 3, 4, 5]
# sum_list = 0
# for counter, i in enumerate(my_list):
#     counter += 1
#     sum_list += i
#
# print(f'Sum: {sum_list} and quantity: {counter}')  # Sum: 15 and quantity: 5
#
# for num in range(10, 0, -1):  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#     print(num)
#
# for i, char in enumerate('Hello'):  # we get index of iterable collection
#     print(i, char)  # 0 H, 1 e, 2 l, 3 l, 4 0

# print(list(range(0, 100, 2)).index(50))  # We are get error when 50 is not exist

# # While loop
# flag = True
# while flag:
#     res = input('Lol: ')
#     if res == 'Lol':    # our break conditional
#         flag = False
#     if res == 'I do not know what to do':
#         pass    # Just to make code executable
#     continue  # move to start of the loop
#
# else:  # if there isn;t a break it'll appear
#     print('And it\'s done')

# # First Python GUI
#
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# # Display the image below to the right hand side where the 0
# # is going to be ' ', and the 1 is going to be '*'.
# # This will reveal an image!
# fill = '$'
# empty = ' '
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end='')
#         else:
#             print(empty, end='')
#     print('')

# # Check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = []
# for item in some_list:
#     if not (item in duplicates):
#         duplicates.append(item)
#     else:
#         print('We have a duplicate in a list!')
#         break
#
# duplicates = []
# for item in some_list:
#     if some_list.count(item) > 1:
#         if item not in duplicates:
#             duplicates.append(item)
#
# print(f'Our duplicates: {duplicates}')

# # Functions
# def say_hello(name):
#     return print(f'Hello {name}')
#
#
# # parameters (default parameters)
# def greet(say_hi=say_hello, name='Tom'):
#     say_hi(name)
#
#
# say_hello('Loli')  # Hello Loli
# # arguments
# # positional arguments -> we need to define a position for arg
# greet(say_hello, 'Andrei')  # # Hello Andrei
# # keyword arguments
# greet(say_hi=say_hello, name='Dan') # Hello Dan
# # default parameters
# greet(name='DNA')  # Hello DNA

# # Best practice
# # Should do one thing rally well.
# # Should return something.
# def my_sum(num1, num2):
#     def another_func(num3, num4):
#         return num3 + num4
#     return another_func(num1, num2)
#
#
# total = my_sum(2, 3)
# print(my_sum(1.2, total))  # 6.2

# # Exercise:
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         return "Sorry, you are too young to drive this car. Powering off"
#     elif int(age) > 18:
#         return "Powering On. Enjoy the ride!"
#     elif int(age) == 18:
#         return "Congratulations on your first year of driving. Enjoy the ride!"
#
#
# age = input("What is your age?: ")
# print(checkDriverAge())  # "Sorry, you are too young to drive this car. Powering off"

# # Methods vs Functions
# # Func:
# def some_random_stuff():
#     pass
#
#
# # Method:
# print('Hello'.count('l'))  # 2

# # Docstrings
# def test(a='aaa') -> None:
#     """
#     Info: this function test and prints param a
#     :param a: aaa
#     :return: None
#     """
#     print(a)
#     return None
#
#
# test('aaa')

# # Clean code
# def is_even(num):
#     return num % 2 == 0
#
#
# print(is_even(51))

# # *args, **kwargs
# # we can easily give to func few parameters(tuple)
# # also we can  transfer a named parameters(dict)
# # Rule: params, *args, default parameters, **kwargs
# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
#
#
# print(super_func(1, 2, 3, 4, 5, num1=10, num2=15))

# # Exercise for highest even:
# def is_even(num) -> bool:
#     return num % 2 == 0
#
#
# def highest_even(li):
#     if li[0]:
#         res_highest_even = 0
#         for item in li:
#             if is_even(item):
#                 if item > res_highest_even:
#                     res_highest_even = item
#         return res_highest_even
#     return None
#
#
# def highest_even_clean(li):
#     even = []
#     for item in li:
#         if item % 2 == 0:
#             even.append(item)
#     return max(even)
#
#
# my_list = [1, 4, 6, 11, 16, 10]
# print(highest_even(my_list))

# # Walrus operator
# a = 'Hellooooooooooo'
# if (b := len(a)) > 10:
#     print(f'Too long {b} elements')
#
# while (n := len(a)) >= 1:
#     print(n, a)
#     a = a[:-1]  # Remove the lat later
#
# print(a)

# Scope - what variables do I have access to?
# Rule:
# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions.
# total = 100  # global scope
#
#
# def some_func(total):
#     # global total  # it's not a good way, just transfer to function
#     local_total = total + 2  # function scope
#
# some_func()
# print(total)

# # nonlocal
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)  # inner: nonlocal
#     inner()
#     print("outer:", x)  # outher: nonlocal
# outer()
