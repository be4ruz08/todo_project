class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        a, b = self.a, self.b
        self.a, self.b = b, a + b
        return a


fib = Fibonacci()
for i in range(10):
    print(next(fib))
