# point = (10, 20)
# print(point[0])
# x = ('john', 10, 30, 'john@gmail.com')


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point1 = Point(x=10, y=20)
# print(point1.x, point1.y)

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# Person = namedtuple('Person', ['name', 'age', 'email'])
# john = Person('John Doe', 18, 'john@gmail.com')
# print(john.name)
#
# print(Person._fields)
# #
# #
# Person = namedtuple('Person', 'name age email', defaults=[20,'john@gmail.com'])
# anna = Person('Anna', 24, 'anna@gmail.com')
# john = Person('John')
# print(john)

# print(Person._fields)
# anna.name = 'Jake'
# print(anna[1])

# my_tuple = (10, 20, 30, ['anna', 'john'])
# my_tuple[3].append('jake')
# print(my_tuple)
# Person = namedtuple('Person', ['name', 'age'])
# person1 = Person(name='John Doe', age=20, children=['anna', 'jake'])
# person1.children.append('tom')
# print(person1)
# data = ('John', 24)
#
# db = {
#     'name': 'Anna',
#     'age': 30
# }
# john = Person._make(data)
# print(john)


# anna = Person(*data)
# print(anna)

# Person = namedtuple("Person", "name age height", defaults=[40, 1.65])
# jane = Person("Jane")
# # john = jane._replace(age=30, name='John')
# print(jane._field_defaults)


Person = namedtuple('Person', 'name age email')


def get_info():

    return Person('John', 20, '<EMAIL>')

john = get_info()

print(f'Name : {john.name} , Age => {john.age}')



# Sequences
message = 'Hello Guys'
# for char in message:
#     print(char, end=' ')

# my_list = [10, 20, 30, 40, 50, 60]
#
# my_list[start,stop,step]
# print(my_list[::-1])


# variable = 'madam'
#
# if variable == variable[::-1]:
#     print('Palindrome')
# else:
#     print('Not Palindrome')

