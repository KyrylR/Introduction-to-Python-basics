# import re

# string = 'search inside of this text this Old Andrei'
#
# print('search' in string)   # True
# pattern = re.compile('search inside of this text this Old')
# print(re.search('this', string))  # <re.Match object; span=(17, 21), match='this'>
#
# a = re.search('this', string)
# print(a.span())  # (17, 21)
#
# print(pattern.findall(string))  # ['search inside of this text this Old']
# print(pattern.match(string))    # <re.Match object; span=(0, 35), match='search inside of this text this Old'>

# pattern = re.compile(r"([a-zA-Z]).([a])")   # r -> for the str to see it like raw
#
# tempStr1 = 'Hello ws a'
# tempStr2 = 'Hi wq a'
#
# # 1: <re.Match object; span=(7, 10), match='s a'> 2: <re.Match object; span=(4, 7), match='q a'>
# print(f'1: {pattern.search(tempStr1)} 2: {pattern.search(tempStr2)}')

# emailValidator = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'a@a.com'
# print(emailValidator.search(string))
#
# password = re.compile(r"((^[a-zA-Z0-9$%#@]{8,24})+\d+$)")
# string = 'asddfdadwd22'
# print(password.fullmatch(string))