A = {}
B = {}
print(type(A))  # puste klamrowe to dict

A = {1, 2, 2, 2, 4}  # pojedyncza cyfra albo po przecinku to set
print(type(A))
print(A)

A = {1: 2137}  # po : znowu dict
print(type(A))

print("______________________________________________")

A = {1, 1, 2, 3, 3, 5}  # jak worek z zawartością
B = {2, 2, 3, 6, 1, 7, 9}

# działania na zbiorach

print(A.union(B))  # nie sortuje wielkością! To tylko czasem się zdarza
print(B.union(A))
print(A.difference(B))
print(B.difference(A))
print(A.difference(B) == A - B)
print(B.difference(A) == B - A)
print(A.intersection(B))

print("-----------------------")


# funkcje ciąg dalszy

def show_arg(*x):  # *x oznacza że nie wiem ile będę chciała mieć parametrów, ale ma przyjąć wszystkie
    return sum(x)


print(show_arg(10, 2, 3))


print("-----------------------")


def suma(*x):
    suma_ = 0
    for element in x:
        suma_ = suma_ + element
    return suma_


print(suma(2, 5, 7))


def dwie_gwiazdki(**kwargs):
    keys = kwargs.keys()
    return keys


d = {"a":1, "b":2}
print(dwie_gwiazdki(**d))


def foo(x=1, y=2):
    return x+y


print(foo())