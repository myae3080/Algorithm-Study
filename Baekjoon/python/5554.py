# math

# input
second_list = []

for i in range(4):
    second_list.append(int(input()))

total_seconds = sum(second_list)

print(total_seconds // 60)
print(total_seconds % 60)