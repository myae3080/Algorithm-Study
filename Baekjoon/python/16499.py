# source : https://www.acmicpc.net/problem/16499
# data structure, string, sorting

dict = {}

for _ in range(int(input())):
    # input
    temp = ''.join(sorted(list(input())))

    if temp not in dict:
        dict[temp] = 0

print(len(dict.keys()))