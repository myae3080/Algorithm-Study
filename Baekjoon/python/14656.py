# input
n = int(input())
stu_list = list(map(int, input().split()))

result = 0

for i, v in enumerate(stu_list):
    if (i + 1) != v:
        result += 1

print(result)