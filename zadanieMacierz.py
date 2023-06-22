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

print("-----------------------------------")

maxi =  list(map(max, matrix))
print(maxi)

print("-----------------------------------")
#średnia arytm


# def mean(row):
#     matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
#     suma = [sum(row) for row in matrix]
#     meanall = [s / 3 for s in suma]
#     return meanall
#
#
# meanall = list(map(mean, matrix))
# print(meanall)

lista_mean = list(map(lambda x: sum(x)/len(x), matrix))
print(lista_mean)

print("-----------------------")

total_sum = sum(map(sum, matrix))
total_count = sum(len(row) for row in matrix)

matrix_mean = total_sum / total_count
print(matrix_mean)