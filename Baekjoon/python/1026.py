# math, sorting

# input
n = int(input())
a_list = sorted(list(map(int, input().split())), reverse=True)
b_list = list(map(int, input().split()))

result = 0

for i in range(n):
    b_max = max(b_list)

    result += a_list.pop() * b_max

    del b_list[b_list.index(b_max)]

print(result)