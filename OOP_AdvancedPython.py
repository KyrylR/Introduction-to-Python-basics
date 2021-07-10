# # Object Oriented Programming
#
# # Create my own class: class -> instantiate -> an instances
# class SomeObj:  # Class
#     pass
#
#
# obj1 = SomeObj()  # instantiate
# print(type(obj1))  # <class '__main__.SomeObj'>


# class PlayerCharacter:  # Class
#     # Class object attribute
#     __membership = True
#
#     def __init__(self, name='anonymous', age=0):  # Constructor
#         self.name = name  # attributes
#         self.age = age
#
#     def run(self):  # method
#         print('run')
#         return 'done'
#
#     def shout(self):
#         print(f'Hello {self.name}')
#
#     @classmethod
#     def add_some(cls, num1, num2):  # we can call by the class, and work with attributes
#         return cls('Taddy', num1 + num2)
#
#     @staticmethod
#     def adding(num1, num2):   # we can call by the class, but we can't work with attributes
#         return num1 + num2
#
#
# player1 = PlayerCharacter('Bob', 12)  # instantiate an obj 'player1'
#
# # print(player1.__membership)  # Error: AttributeError: 'PlayerCharacter' object has no attribute '__membership'
#
# print(player1)  # <__main__.PlayerCharacter object ...>
# print(type(player1.age), player1.age)  # <class 'int'>, 12
# print(player1.run())  # run \n done
# player1.shout()  # Hello Bob
#
# player3 = PlayerCharacter.add_some(3, 5)  # create an obj 'player3', name = Taddy, age = 3 + 5 = 8
# player3.shout()  # Hello Teddy
# print(PlayerCharacter.adding(3, 5))  # 8


#
# # help(list)  # shows everything that available to use

# # Exercise:
# class Cat:
#     _species = 'mammal'
#
#     def __init__(self, name="None", age=0):
#         self.name = name
#         self.age = age
#
#
# # My function
# def find_oldest_cat(*args):
#     oldest_cat = args[0]
#     for cat in args:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat
#
#
# # Much cleaner
# def get_oldest_cat(*args):
#     return max(args)
#
#
# cat1 = Cat("cat1", 16)
# cat2 = Cat("cat2", 18)
# cat3 = Cat("cat3", 15)
#
# print(find_oldest_cat(cat1, cat2, cat3).name)
# print(get_oldest_cat(cat1.age, cat2.age, cat3.age))

# # We always need to test our assumptions
# class SomeClass:
#     def __init__(self, name):
#         self._name = name
#
#     def do_smth(self):
#         print(self._name)
#         return self
#
#     @property
#     def name(self):
#         return self._name
#
#
# temp = SomeClass('New')
# print(temp.name)  # we have a property to work with it by convention
# print(temp is temp.do_smth())  # New \n True

# # Inheritance
# class SupperClass:
#     @staticmethod
#     def func():
#         print('Supper')
#
#
# # SubClass inherit SupperClass
# class SubClass(SupperClass):
#     pass
#
#
# SubClass.func()
# sub = SubClass()
# print(isinstance(sub, SupperClass))  # True
# print(isinstance(sub, object))  # True
#
# # 4 Pillars of OOP:
# #   - Encapsulation
# #   - Abstraction
# #   - Inheritance
# #   - Polymorphism

# # Inheritance exercise and also continue lectures:
# class Pets(object):
#     animals = []
#
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#     def __len__(self):  # overwrite len()
#         return len(self.animals)
#
#     def __getitem__(self, item):  # overwrite []
#         return self.animals[item]
#
#
# class Cat(object):
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#     def __str__(self):  # overwrite str()
#         return f'Name: {self.name}'
#
#     def sing(self):
#         return f'{self.name}: "None"'
#
#     def __call__(self):  # overwrite ()
#         return self.sing()
#
#
# class Simon(Cat):
#     def __init__(self, name, age, sound):
#         # Call parent __init__
#         super().__init__(name, age)  # don't worry about passing self.
#         self.sound = sound
#
#     def sing(self):
#         return f'{self.name}: {self.sound}'
#
#
# class Sally(Cat):
#     def __init__(self, name, age, sound):
#         # Call parent __init__
#         super().__init__(name, age)  # don't worry about passing self.
#         self.sound = sound
#
#     def sing(self):
#         return f'{self.name}: {self.sound}'
#
#
# class Alex(Cat):
#     def __init__(self, name, age, sound):
#         # Call parent __init__
#         # Cat.__init__(self, name, age)
#         super().__init__(name, age)  # don't worry about passing self.
#         self.sound = sound
#
#     def sing(self):
#         return f'{self.name}: {self.sound}'
#
#
# # Introspection
# my_cats = [Simon('Bob', 12, 'I - Bob'), Sally('Alex', 5, 'I - ALex'), Alex('Fio', 14, 'Wow')]
# pets = Pets(my_cats)
#
# # Bob is just walking around
# # Alex is just walking around
# # Fio is just walking around
# pets.walk()
#
# print(str(pets[2]))  # Name: Fio
# print(pets[0]())  # Bob: I - Bob
# print(len(pets))  # 3
# print(dir(pets))  # To what we have an access


# # We can easily have a multiple inheritance
# # P.S: Make it logical with __init__ in SubClass
# class SupperList(list, object):
#     def __len__(self):
#         return 1000
#
#
# my_list = SupperList([32, 1])
# my_list.extend([12, True, 'LIS'])
# print(my_list)  # [32, 1, 12, True, 'LIS']
# print(len(my_list))  # 1000
# print(issubclass(SupperList, list))  # True
# print(issubclass(list, object))  # True


# # MRO - method resolution order
# class A:
#     num = 10
#
#
# class B(A):
#     num = 1
#
#
# class C(A):
#     num = -1
#
#
# class D(B, C):
#     pass
#
#
# print(D.mro())  # Output:
# # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
