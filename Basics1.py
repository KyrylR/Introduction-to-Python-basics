# # Python intro in ZtoM
#
# # Learning a language: terms(variables and ect), actions, data types, best Practices.
#
# # Fundamental Data type.
# int
# float
# bool
# str
# list
# tuple
# set
# dict
#
# # Classes -> custom types.
#
# # Specialized Data Types. Example: modules
#
# None
#
# # int and float
# print(2 + 4)  # 6, same with *, /, -
# print(type(1 + 3))  # <class 'int'>
# print(2 ** 3)  # 8 pow
# print(12 % 10)  # 2  mod
# print(5 // 3)  # 1 div
# print(type(0.0))  # <class 'float'>
# print(4E4)  # 4000.0 (float)
# print(divmod(12, 10)) # the pair (x // y, x % y)
# # source https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#
# # math functions. https://www.programiz.com/python-programming/modules/math
#
# print(round(0.5648, 3))  # 0.565
# print(abs(-10))  # 10
#
# # Developer fundamentals:
# # - Don't read the dictionary;
# # - Name things well;
# # - Use Documentation to your code;
# # - Understanding Data Structures.
# # - Clean code:
# #   * Readability
# #   * Predictability
# #   * DRY -> Don't repeat yourself
# #   * Make code reusable
# # - Test your assumptions
#
#
#
# # Operator precedence () -> ** -> *, / -> +, -
#
# print((20 - 3) * 2 ** 3 - 1)  # 135
#
# # Complex
# complex
# print(complex(2, 2))  # (2+2j)
#
# print(bin(5))  # 0b101
# print(int('0b111', 2))  # 7
#
# # constants -> never change
# # assign vars
# a, b, c = 1, 2, 3  # a = 1, b = 2, c = 3
#
# # Expression: some / 3
# some = 141
# less = some / 3  # less = 47
# # Statement: less = some / 3
#
# # augmented assignment operator
# some_val = 5
# some_val += 2  # equal some_val = some_val + 2
#
# # Strings
# print(type('Lol') == type("Lol"))  # True
# long_str = ''' Wow
# asd
# dsd
# '''  # Long string(with paragraph)
#
# _str = 'mam'
# print(f'Kiril and {_str} ' + _str)  # Formatted str; Easily concat strings(str + str);
# print(str(100) + " is not a number")  # possible error: str + int and ect.
#
# # Escape Sequence \t - tab, \n - new line, \b - ascii backspace
# weather = 'It\'s suu\bnny'
# print(weather)  # It's sunny
#
# name = 'Johnny'
# age = 55
# # Easily to print int without str parse function
# print(f'Hi {name}; age {age}')  # Hi Johnny; age 55
#
# selfish = 'mem lol no it\'s you'
# print(selfish.split())  # ['mem', 'lol', 'no', "it's", 'you']
# print(selfish.split('\''))  # ['mem lol no it', 's you']
#
# # [start:end:step]
# numbers = '0123456789'
# print(numbers[::-1])  # 9876543210
# print(numbers[1:7:2])  # 135
#
# # Check for cycle word; True
# cycle_word = "12321"
# if cycle_word.find(cycle_word[::-1]):
#     print(False)
# else:
#     print(True)
#
# # Immutability
# # selfish = 'lol'
# # selfish[0] = '10'  # Error
#
# # Built-in functions and methods
# # For str: jem and ect.
# print(len('0123'))  # 4
#
# hamlet = 'to be or not to be'  # methods replace, find, index and ect for str.
# print(hamlet.index('or', 6, len(hamlet)))  # index vs find: Error or -1 respectively
#
# # Booleans
# tr = False
# print(tr.as_integer_ratio())  # (0, 1)
# print(tr.bit_length())  # 0
#
# # Program that return your age by inputting your year of birth
# from datetime import date
# birth_year = int(input('what year wee you born?\n'))
# print(f"Your age: {int(date.today().strftime('%Y')) - birth_year}")
#
#
# # Check password program P.S.: works only in cmd!
# from getpass import getpass
# password = getpass()
# pass_len = len(password)
# hidden_pass = '*' * pass_len
# print(f'Your password: {hidden_pass} is {pass_len} long.')
#
#
# # Data structure
# # List
# li = [1, 2, '3', True, 'wow']
# li[2] = '4'  # lists are mutable
# new_list = li[:]  # To copy list
# new_list[0] = -1  # So as we can see, parent list wasn't changed
# print(new_list)  # [-1, 2, '4', True, 'wow']
# print(li)  # [1, 2, '4', True, 'wow']
#
# li.append(False)
# li.remove('4')
#
# print(f'Count: {li.count(1)}')  # Count: 2
# print(li.pop(0))  # 1
# # Easily cam use [start:end:step] <- slicing
# print(li[::1])  # [2, True, 'wow', False]
# # Also can use built-in func but not every.
# print(len(li))  # 4
#
# # Matrix -> just multidimensional arrays
# matrix = [
#     [7, 8, 9],
#     [3, 2, 1],
#     [4, 5, 6],
# ]
#
# sorted(matrix)  # not sort an matrix
# print(matrix)  # [[7, 8, 9], [3, 2, 1], [4, 5, 6]]
#
# matrix.sort()  # sort matrix instead of built-in func sorted()
# print(matrix)  # [[3, 2, 1], [4, 5, 6], [7, 8, 9]]
#
# print(1 in matrix[0])  # ref to find vs index; True
#
# # Check for cycle word
# cycle_word = '12331'
# print(cycle_word[::-1] in cycle_word)  # True
#
# # Range
# print(list(range(1, 100, 10)))  # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
#
# # Join
# sentence = ' '
# print(sentence.join(['Hi', 'Bob', '\b,', 'it\'s sunny']))  # Hi Bob, it's sunny
# print('Sen: ' + sentence)  # Sen:  \0
#
# # List unpacking
# first, *mid, last = [1, 2, 3, 4, 5]
# print(first)  # 1
# print(mid)  # [2, 3, 4]
# print(last)  # 5
#
# # None
# a = None
# print(type(a))  # <class 'NoneType'>
#
# # Dictionary
# # Keys in dict can not change! data structure must be immutable
# dictionary = {
#     'a': 1,
#     (1, 2): 2  # (1, 2) tuple
# }
#
# print(dictionary.get((1, 2)))  # 2; dictionary do not change
# print(dictionary.pop((1, 2)))   # 2; dictionary changed, 2 was removed
# # Returns a default value
# print(dictionary.pop('d', 'Sorry it\'s not exist yet!'))  # Sorry it's not exist yet!;
# # Returns a default value
# print(dictionary.get((1, 2), "It was 2 :)"))  # It was 2 :)
# print(dictionary.update({'c': ['a', 'b'], 'd': False}))  # Update dict, return None.
# print(dictionary.items())  # dict_items([('a', 1), ('c', ['a', 'b']), ('d', False)])
# print(dictionary.keys())  # dict_keys(['a', 'c', 'd'])
# print(dictionary.values())  # dict_values([1, ['a', 'b'], False])
#
# print(1 in dictionary.values())  # True
# dictionary.clear()  # {}

# # Try to sort dictionary
# my_dictOrder = {
#     1: 'a',
#     2: 'b',
#     4: 'd',
#     3: 'c'
# }
#
# print(sorted(my_dictOrder))  # we will receive list

# # Tuple -> immutable list
# my_tuple = (10, 1, 2, '3', 4, 5, 5)
# print(my_tuple.index(10))  # 0
# print(5 in my_tuple)  # True
# print(my_tuple[::])  # (10, 1, 2, '3', 4, 5, 5)
# print(my_tuple.count(5))  # 2
#
# # Set -> unordered collection of unique objects, also immutable
# my_set = {10, 1, 9, 4, 3, 3}
# print(my_set)  # {1, 3, 4, 9, 10}
# print(my_set.difference({1, 2, 3, 4}))  # {9, 10}
#
# print(my_set.discard(3))  # None
# print(my_set)  # {1, 4, 9, 10}
#
# # equals print(my_set & {1, 2})
# print(my_set.intersection({1, 2, 3, 4}))   # {1, 4}
#
# print(my_set.isdisjoint({2, 13}))  # True
# print(my_set.issubset({1, 4, 9, 10, 11, 14})) # True
# print(my_set.issuperset({1, 4, 9})) # True
#
# # equals print(my_set | {1, 2})
# print(my_set.union({1, 2}))  # {1, 2, 4, 9, 10}
#
# my_list = [1, 2, 3, 3, 3]
# print(my_list)  # [1, 2, 3, 3, 3]
# my_list = list(set(my_list))
# print(my_list)  # [1, 2, 3]
