# sorting

# input
n = int(input())

num_set = set()

[num_set.add(int(i)) for i in input().split()]

print(str(sorted(num_set)).replace('[', '').replace(']', '').replace(',', ''))