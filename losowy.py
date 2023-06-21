import random
from collections import Counter

random.seed(42)
value = random.random()


print(value)
# for line in dir(random.random()):
#     print(line)

fruits = ["grapes", "oranges", "berries", "bananas"]

fruits_random = random.choice(fruits)

print(fruits_random)

# random.shuffle(fruits)
#
# my_counter = Counter(fruits)

# print(fruits)

# for i in range (1, 24):
# my_counter = Counter(fruits)
# random_fruits = random.shuffle(my_counter)
#     # print(my_counter)
# print(random_fruits)
#
