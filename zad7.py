import random


# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
#
# even_numbers = all_even()
#
# print(next(even_numbers))

def generate_password(dlugosc_hasla):
    new_password = ''
    for i in range(dlugosc_hasla):
        new_password += chr(random.randint(33, 126))

    yield new_password


password_generator = generate_password(100)

print(next(password_generator))
