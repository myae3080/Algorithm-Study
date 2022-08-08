# source : https://www.acmicpc.net/problem/17614

# input
n = int(input())

print(sum([str(i).count('3') + str(i).count('6') + str(i).count('9') for i in range(1, n + 1)]))