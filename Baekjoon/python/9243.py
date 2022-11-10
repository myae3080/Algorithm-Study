# source : https://www.acmicpc.net/problem/9243

# input
n = int(input())
before, after = input(), input()

is_deleted = True
if n % 2 == 0:
    if before != after:
        is_deleted = False
else:
    for i in range(len(before)):
        if before[i] == after[i]:
            is_deleted = False
            break
        
print('Deletion succeeded') if is_deleted else print('Deletion failed')