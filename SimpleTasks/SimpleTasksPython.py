import sys

print(sys.version)
print(sys.executable)


# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).The numbers
# obtained should be printed in a comma-separated sequence on a single line.

# def find_special_num():
#     nums = []
#     for i in range(2000, 3201):
#         if i % 7 == 0 and i % 5 != 0:
#             nums.append(i)
#     return nums
#
#
# print(find_special_num(), end=',')
#
# print((i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")


# Write a program which can compute the factorial of a given numbers.The results
# should be printed in a comma-separated sequence on a single line.Suppose the
# following input is supplied to the program: 8 Then, the output should be:40320
#
# from functools import reduce
#
# while True:
#     try:
#         num = int(input('Input number: '))
#         print(reduce(lambda acc, item: acc * item, range(1, num + 1)))
#     except ValueError:
#         print('Please input number')
#     except TypeError:
#         print('Please enter non negative number')
#     except Exception as err:
#         print(err, type(err))
#     else:
#         print('Thanks')
#         break

# With a given integral number n, write a program to generate a dictionary that
# contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should
# print the dictionary.Suppose the
# following input is supplied to the program: 8

#
# while True:
#     try:
#         num = int(input('Input number: '))
#         dictionary = {key: key * key for key in range(1, num + 1)}
#         print(dictionary)
#     except ValueError:
#         print('Please input number')
#     except Exception as err:
#         print(err, type(err))
#         print('Lol')
#     else:
#         print('Thanks')
#         break

# Task 4: Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
#
# ls = input('Write nums: ').replace(' ', '').split(',')
# print(ls)
# print(tuple(ls))

# Task5:
#
# Define a class which has at least two methods:
#     getString: to get a string from console input
#     printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class Sample(object):
#     def __init__(self, string):
#         self.string = string
#
#     def getString(self):
#         self.string = input('Enter String: ')
#
#     def printString(self):
#         print(str(self.string).upper())
#
#
# sample = Sample('Hello')
# sample.printString()
# sample.getString()
# sample.printString()


# Task 6
#     Write a program that calculates and prints the value according to the given formula:
#     Q = Square root of [(2 _ C _ D)/H]
#     Following are the fixed values of C and H:
#     C is 50. H is 30.
#     D is the variable whose values should be input to your program in a comma-separated sequence.

# from math import sqrt
#
# C, H = 50, 30
#
#
# def calc(D):
#     return sqrt((2 * C * D) / H)
#
#
# # D = [int(i) for i in input().split(' ')]  # splits in comma position and set up in list
# # D = [int(i) for i in D]  # converts string to integer WET!!!!!
# # D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
# # D = [round(i) for i in D]  # All the floating values are rounded
# # D = [str(i) for i in D]  # All the integers are converted to string to be able to apply join operation
#
# # print(", ".join(D))
#
# D = [str(int(calc(int(i)))) for i in input().split(' ')]
# print(", ".join(D))


def array_nesting(nums: list[int]) -> int:
    output = 0

    for i in range(len(nums)):
        tmp = 1
        last_i = i
        i = nums[i]
        while i != last_i:
            i = nums[i]
            tmp += 1
        output = max(output, tmp)
    return output


print(array_nesting([2, 3, 1, 4, 0, 5]))
