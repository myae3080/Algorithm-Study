# brute force

# input
num_count, target_num = map(int, input().split())

count = 0

'''
    두 번째 풀이
'''
for n in range(1, num_count + 1):
    count += str(n).count(str(target_num))

print(count)

'''
    첫 번째 풀이
    너무 느림
'''
for n in range(1, num_count + 1):
    for s in str(n):
        if s == str(target_num):
            count += 1

print(count)