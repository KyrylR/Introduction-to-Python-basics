# # Functional Programing (Separation of concerns)
# #   - Pure functions
# #   -
# #   -
# #
# # Pure functions
# #   - Given the same input, it will always return
# #     the same output that is, every time we give
# #   - Function should not produce any side effects
#
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
#
# print(multiply_by2([1, 2, 3]))

# # Useful functions: map, filter, zip and reduce
#
# # map
# def multiply_by2(item):  # we just need an action; what effect we want to produce
#     return item * 2
#
#
# my_list = [1, 2, 3]
# # map call the func for us and make NEW list with some effect of
# # doing something and take a result
# print(list(map(multiply_by2, my_list)))  # [2, 4, 6]
# print(my_list)  # Does not change anything outside the world
#
#
# # filter
# def only_odd(item):
#     return item % 2 != 0
#
#
# my_list = [1, 2, 3, 4]
# # filter call the func for us and make NEW list with some effect
# # if TRUE it'll be add to new list, or opposite if FALSE!
# print(list(filter(only_odd, my_list)))  # [1, 3]
# print(my_list)  # Does not change anything outside the world
#
# # zip
# first_list = [1, 2, 3, 4]
# second_list = (10, 20, 30, 40, 50)
# third_list = {-1, -2, -3}
#
# # Take first elem of first list and first elem of second list and ....
# # and zips(connect) them, into: [(), (), ...]
# print(list(zip(first_list, second_list, third_list)))  # [(1, 10, -3), (2, 20, -1), (3, 30, -2)]
#
# # reduce
# from functools import reduce

#
# def accumulator(acc, item):
#     return acc + item
#
#
# my_list = [1, 2, 3, 4]
# # We go threw over our list with the last returned value
# print(reduce(accumulator, my_list, 0))

# # Exercise:
# # 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
#
# def capitalize_words(item):
#     return str(item).capitalize()
#
#
# print(list(map(capitalize_words, my_pets)))
#
# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
#
# print(list(zip(sorted(my_numbers), my_strings)))
#
#
# # 3 Filter the scores that pass over 50%
# def bigger_then_50pers(item):
#     return item > 50
#
#
# scores = [73, 20, 65, 19, 76, 100, 88]
# print(list(filter(bigger_then_50pers, scores)))
#
#
# # 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the
# total?
# def combine(acc, item):
#   return acc + item
#
#
# print(reduce(combine, (my_numbers + scores)))

# # Lambda expressions, we not need more than once
# my_list = [1, 2, 3]
#
# print(list(map(lambda param: param * 2, my_list)))  # Just use simple(pure) function
# print(list(filter(lambda param: param % 2 != 0, my_list)))
# print(reduce(lambda acc, item: acc + item, my_list))

# # Exercise
# my_list = [5, 4, 3]
# print(list(map(lambda param: param ** 2, my_list)))
#
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)

# # Comprehensions: list, set, dictionary
# my_list = [char for char in 'hello']
# print(my_list)  # ['h', 'e', 'l', 'l', 'o']
#
# my_set = {char for char in 'hello'}
# print(my_set)   # {'l', 'o', 'h', 'e'}
#
# list_nums = [num * 2 for num in range(0, 100)]
# print(list_nums)    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, ....
#
# list_even_nums = [num ** 2 for num in range(0, 100) if num % 2 == 0]
# print(list_even_nums)   # [0, 4, 16, 36, 64, 100, 144, 196, 256, ....
#
#
# list_nums = [num for num in range(0, 30)]
# list_letters = [chr(char) for char in range(97, 123)]
# my_dict = {key: value ** 2 for key, value in list(zip(list_letters, list_nums)) if value % 2 == 0}
# print(my_dict)  # {'a': 0, 'c': 4, 'e': 16, 'g': 36, 'i': 64,
#
# my_dict = {num: num * 2 for num in range(1, 10) if num % 2 != 0}
# print(my_dict)  # {1: 2, 3: 6, 5: 10, 7: 14, 9: 18}

# # Check for duplicates
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = list({char for char in some_list if some_list.count(char) > 1})
# print(duplicates)
