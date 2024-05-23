# class Fibonacci:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         fib = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return fib
#
#
# fib = Fibonacci()
# for i in range(10):
#     print(next(fib))


def fibonacci_generator():
    a = 0
    b = 1
    try:
        while True:
            try:
                result = yield a
                if result is not None:
                    a, b = result
            except Exception as e:
                print(e)
                raise
            a, b = b, a + b
    finally:
        print("Successfully generated")


gen = fibonacci_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(gen.send((21, 34)))
print(next(gen))
print(next(gen))


try:
    gen.throw(ValueError)
except ValueError:
    print("ValueError")

gen.close()



