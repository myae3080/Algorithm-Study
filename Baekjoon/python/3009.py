# math, geometry

# input
x_list, y_list = [], []

for i in range(3):
    x, y = map(int, input().split())

    x_list.append(x)
    y_list.append(y)

print([x_list[i] for i in range(3) if x_list.count(x_list[i]) == 1][0], [y_list[i] for i in range(3) if y_list.count(y_list[i]) == 1][0])