# class PowTwo:
#     def __init__(self, max = 0):
#         self.n = 0
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration
#
#         result = 2 ** self.n
#         self.n += 1
#         return result
#
#
# a = PowTwo(4)
#
# for i in range(3):
#     print(next(a))
#
#
# print("________________________________________")
#parzyste od 200 do 100 i zeby zatrzymal sie jak schodzi ponizej 100


class PowTwoFrom200:
    def __init__(self, max=100):
        self.n = 200
        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration

        result = self.n
        self.n -= 2
        self.count += 2
        return result


a = PowTwoFrom200(100)

for i in range(100):
    print(next(a))
