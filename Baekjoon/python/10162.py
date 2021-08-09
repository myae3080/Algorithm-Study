# source : https://www.acmicpc.net/problem/10162
# math, greedy

sec_list = [300, 60, 10]
result = []

# input
sec = int(input())

for s in sec_list:
    result.append(str(sec // s))

    sec %= s

print(' '.join(result)) if sec == 0 else print(-1)