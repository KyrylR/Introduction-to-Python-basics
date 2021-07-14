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

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the
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
#     else:
#         print('Thanks')
#         break
