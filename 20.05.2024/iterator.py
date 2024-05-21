# arr = [10, 20, 30, 40, 50] # List collections
# for i in arr:
#     print(i)
from datetime import datetime
from typing import Optional

my_tuple = (10, 20, 30)  # tuple

my_dict = {'username': 'john', 'age': 24}  # dict
# for key in my_dict:
#     print(key)

my_set = {'olma', 'anor', 'banan'}  # set

# for fruit in my_set:
#     print(fruit)


# Iterable vs Iterator

# my_list = [10, 20, 30, 40, 50]
# iter and next
#
# variable = iter(my_list)
# print(next(variable))
# print(next(variable))
# print(next(variable))
# print(next(variable))
# print(next(variable))
# print(next(variable))
# my_list = [10, 20, 30, 40, 50]
# # for i in my_list:
# #     print(i)
#
#
# iterator = iter(my_list)
# try:
#     while True:
#         print(next(iterator))
#
# except StopIteration:
#     pass
# arr = [10, 20, 30, 40, 50, 60]
# _index = 0
#
# while _index < len(arr):
#     item = arr[_index]
#
#     _index += 1
#     print(item)


# my_alphabet = ['a', 'b', 'c', 'd']
# iterator = iter(my_alphabet)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# car = {
#     'name': 'Cobalt',
#     'color': 'black',
#     'price': 13_000,
#     'created_at': datetime.now()
# }
#
# key = iter(car)
# try:
#     while True:
#         print(next(key))
#
# except StopIteration:
#     pass
# import string
#
# my_alphabet = string.ascii_lowercase
# iterator = iter(my_alphabet)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# print(chr(84))

# my_list = [chr(i) for i in range(97, 123)]
#
# iterator = iter(my_list)
# try:
#     while True:
#         print(next(iterator))
#
# except StopIteration:
#     pass
#
# class Counter:
#     def __init__(self, current, end):
#         self.current = current
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#
#         item = self.current
#         self.current += 1
#         return item
#
#
# counter = Counter(50, 20)
# # for i in counter:
# #     print(i)
# print(next(counter))
# print(next(counter))

# class CustomIterator:
#     def __init__(self, sequence):
#         self._index = 0
#         self._sequence = sequence
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self._sequence):
#             raise StopIteration
#         else:
#             item = self._sequence[self._index]
#             self._index += 1
#             return item

# obj = CustomIterator(('10,20,30,40',))
# for i in obj:
#     print(i)
#
# for i in obj:
#     print(i)

# class MyIterator:
#     def __init__(self, start):
#         self.start = start
#         self.step = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         item = self.start
#         self.start += self.step
#         return item
#
#
# my_iterator = MyIterator(2)
# for i in my_iterator:
#     print(i)


class MyRange:
    def __init__(self, start, stop, step: Optional[int] = None):
        self.start = start
        self.step = step or 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item
        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item


obj = MyRange(2, 14, 1)
for i in obj:
    print(i)

with open('db.txt') as file:
    data = file.readlines()
    # for i in file:
    #     print(i)
    for i in data:
        print(i)


# Fibonacci
