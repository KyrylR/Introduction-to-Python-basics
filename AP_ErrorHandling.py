# # Error Handling
# #
# # Syntax Error:
# # def hoho()
# #     pass
# #
# # Name Error:
# # 1 + name
# #
# # Index Error:
# # li = [1, 2]
# # li[2]
# #
# # Type Error:
# # print(1 + 'hi')
# #
# # KeyError:
# # di = {'a':1}
# # print(di['b'])
# #
# # ZeroDivisionError:
# # 5/0
# #
# # And ect...
# #
# # Error Handling

# while True:
#     try:
#         age = int(input('How old are you?\n'))
#         a = 12/age
#         print(age)
#     except ValueError:
#         print('Pease, enter a number!')
#         # raise Exception('WOOOOW')   # stop program and show exception
#     # except ValueError:  # Will not run
#     #     print('Pease, enter a number!')
#     except ZeroDivisionError:
#         print('Please do not enter a 0')
#     except Exception as err:
#         print(err)
#     else:
#         break
#     finally:
#         print('Ok, I am finally done')
#     print('can you here me')
#
# def addition(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'{err}')
#
#
# print(addition("1", 0))
