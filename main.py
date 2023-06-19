# x = 1
# print (x)

# for i in range(1, 12):
#     print("Wartość iteratora to" + str(i))

# for i in range(10):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)
#
# for i in range(1, 20, 2):
#     print(i)

# lista = ["a", "b", "c", "d"]
# for element in lista:
#     print(element)
#
# print("________________")
#
# N = len(lista)
# for i in range(N):
#     print(lista[i])

# i = 0
# while (i < 11):
#     print(i)
#     i = i + 1

# Zad 1 Wypisz liczby od 0 do 10 które są podzielne przez 6
# for i in range(0, 101):
#     if i % 3 == 0:
#         if i % 2 == 0:
#             print(i)

for i in range(0, 101, 6):
    print(i)

print("-------------------------------")

s1 = "Ala ma kota"
print(s1[:4])
print(s1[4:])

if s1[:4] + s1[4:] == s1:
    print("Prawda")

print("-------------------------------")

s1 = "Ala ma kota"
print(len(s1))
print("Długość łańcucha to {len(s1)}")

print("-------------------------------")
s1 = "Ala ma kota"
print(s1.split("a"))

print([x for x in s1.split("a") if x != ""])

lista2 = []
for x in s1.split("a"):
    if x != " ":
        print(lista2.append(x))

print("-------------------------------")

s1 = "Ala ma kota"
print(s1.replace(" ", "_"))
print(s1.find("a"))

print("-------------------------------")

szukany_znak = "a"
for index, word in enumerate(s1):
    if word == szukany_znak:
        print(index)

print("-------------------------------")

print(" Ala".strip() in s1)

print("-------------------------------")

print(" Ala".lstrip())  # jak damy rstrip to z prawej odcina jeżeli jest spacja

print("-------------------------------")

print("Ala" * 5)

print("-------------------------------")

# zapytanie = input("Podaj swój nr tel")
# zapytanie = int(zapytanie)

print("-------------------------------")

lista1 = [1, 2, 3]
lista2 = [11, 13, 15]

lista3 = []
for ind1, el1 in enumerate(lista1):
    for ind2, el2 in enumerate(lista2):
        if ind1 == ind2:
            print(lista3.append(el1 + el2))

print("-------------------------------")

lista4 = [2, 1, 3, 7]
print(sorted(lista4))  # na stale, napisujemy
print(lista4.sort())  # na chwile

print("-------------------------------")

print("+".join(("kaczka", "piemsek")))

print("-------------------------------")

wartosci = ['Nowa nadzieja', 'Imperium kontratakuje', 'Powrót Jedi']
klucze = [4, 5, 6]
print(list(zip(wartosci, klucze)))  # do szukania po indexach
print(dict(zip(wartosci, klucze)))  # do szukania po nazwach

lista5 = [2, 1, 3, 7]
lista5[0] = 99
print(lista5)

print("-------------------------------")


# funkcje

def kwadrat(x):
    return x ** 2


for i in range(10):
    print(kwadrat(i))


def foo(x, y):
    return x, y


result = foo(4, 3)

print("------------------------")


def delta(a, b, c):
    dzial = b ** 2 - 4 * a * c
    if dzial == 0:
        return 1
    elif dzial > 0:
        return 2
    else:
        return 0


print(delta(1, 2, 1))


# funkcje lambda

def kwadrat(x):
    print(x ** 2)


kwadrat2 = lambda x: x ** 2

print(kwadrat2(9))

print("--------------------------")

lista6 = [2, 1, 3, 7]
for x in lista6:
    print(x, kwadrat2(x))

print(list(map(kwadrat2, lista6)))

cube = lambda x: x ** 3
print(list(map(cube, lista6)))


def kaszanka(x):
    return 2 * x + 1


print(list(map(kaszanka, lista6)))

lista7 = [-1, 0, 2, -6, 10]
print(list(filter(lambda x: x if x > 0 else "", lista7)))


from functools import reduce
silnia = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x*y, silnia))

lista8 = [2, 1, 3, 7]
print([x**2 for x in lista8])