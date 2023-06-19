# data = open("C:\\Users\\owiczlin\\Downloads\\dane.txt")
# # data_str = data.read()
# data_line = data.readlines()
# print(data_line)
# print(len(data_line))

path = "C:\\Users\\owiczlin\\Downloads\\dane.txt"
# with open(path, 'r') as f:
#     reader = f.readlines()
#     for line in reader:
#         print(line.split(" ")[1], line.split(" ")[3][1:-1])
#         f.close()

data = open(path)
data_line = data.readlines()

suma = 0
for i in data_line:
    x = i.split(" ")
    banned = ["-", ",", ".", ":" , ";"]
    x = list(filter(lambda x: x if x not in banned else False, x))
    print(x)
    print(len(x))

    print(suma)