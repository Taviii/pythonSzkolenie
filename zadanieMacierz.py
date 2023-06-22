matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)

a = [[row * 3 + col + 1 for col in range(3)] for row in range(1)]
b = [[row * 3 + col + 1 for col in range(3, 6)] for row in range(1)]
c = [[row * 3 + col + 1 for col in range(6, 9)] for row in range(1)]

suma = sum(sum(row ) for row in matrix)
suma3 = [sum(row) for row in matrix]
print(suma)
print(suma3)

print("--------------------------------")

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)

matrix_sum = 0
for row in matrix:
    for num in row:
        matrix_sum += num

print(matrix_sum)