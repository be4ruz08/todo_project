# arr = [10, 20, 30, 40, 50] # List collections
# for i in arr:
#     print(i)
from datetime import datetime

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
#
#
# alphabet = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#     'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
#
# iterator = iter(alphabet)
#
# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     pass



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

class CustomIterator:
    def __init__(self, sequence):
        self._index = 0
        self._sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        else:
            item = self._sequence[self._index]
            self._index += 1
            return item


obj = CustomIterator('10,20,30,40')

for i in obj:
    print(i)

