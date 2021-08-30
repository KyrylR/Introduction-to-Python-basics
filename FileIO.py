# # File I/O(input/output)
#
# # We created a new file in Terminal by notepad
# my_file = open('test.txt')
# print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
# print(my_file.read(1))  # a (aaa -> in File)
# print(my_file.read(1))  # aa (aaa -> in File)
#
# print(my_file.readlines())  # list with all lines in file
#
# my_file.close()  # After we end work with file, we need to close it!

# # Modes:
# # r -> read
# # w -> write    (creat or override)
# # r+ > read and write
# # a -> append
# # x - Create - will create a file, returns an error if the file exist
# with open('Modules\\sad.txt', mode='r+') as my_file:  # if we use this statement we do not need to close a file
#     # directly
#     # text = my_file.write(':(')
#     # print(text)
#     print(f'My file: \n{my_file.readlines()}')

# # P.S We can use built in module like pathlib to make our programme computable

# # Common way to work with files:
# try:
#     with open('sad.txt') as my_file:
#         print(my_file.readlines())
# except FileNotFoundError as err:
#     print('File do not exist')
#     raise err
# except IOError as err:
#     print('IO error')
#     raise err

# # Exercise: Translator
# from translate import Translator
#
# translator = Translator(to_lang='de')
#
# try:
#     with open('test.txt', mode='r+') as tr_file:
#         file_text = tr_file.read()
#         translation = translator.translate(file_text)
#         tr_file.write(f'\nYour translation:\n{str(translation)}')
# except FileNotFoundError as err:
#     print('File do not exist')
#     raise err
# except IOError as err:
#     print('IO error')
#     raise err
