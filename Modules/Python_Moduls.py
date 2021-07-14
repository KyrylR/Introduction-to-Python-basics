from Modules.utility import divide, multiply, Student    # or we can use * instead of divide, multiply
from Shopping.shopping_cart import buy


stud1 = Student()
print(type(stud1))  # <class 'Modules.utility.Student'>

if __name__ == '__main__':
    print(__name__)     # __main__
    print(divide(2, 2))  # 1.0
    print(multiply(2, 2))  # 4
    print(buy({3, 2, 1}))  # [{1, 2, 3}]