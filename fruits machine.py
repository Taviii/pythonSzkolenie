import random
from collections import Counter

fruits = ["grapes", "oranges", "berries", "bananas"]

kopia_f = fruits[:]
lista = []
for i in range(24):
    kopia_f_copy = kopia_f.copy()
    random.shuffle(kopia_f_copy)
    lista.append(kopia_f_copy)

counts = Counter(tuple(combination) for combination in lista)

for combination, count in counts.items():
    print(combination, ":", count)