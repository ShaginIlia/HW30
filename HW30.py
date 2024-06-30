class EvenNumbers:

    def __init__(self, start, end):
        self.start, self.end = start, end

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i > self.end:
            raise StopIteration
        else:
            if self.i % 2 == 0:
                res = self.i
                self.i += 2
                return res
            else:
                self.i += 1
                return self.__next__()


en = EvenNumbers(10, 25)
for i in en:
    print(i)
