lista1 = [4, 6]
lista2 = [3, 5]


def scalar_product(lista1=None, lista2=None):
    result = 0
    for x, y in zip(lista1, lista2):
        result += x * y
    return result


print(scalar_product(lista1, lista2))
