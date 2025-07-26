class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1



    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        print(self.a)
        print(self.b)
        return fib

fbs = Fibs()
for f in fbs:
    if f > 1000:
        print(f)
        break