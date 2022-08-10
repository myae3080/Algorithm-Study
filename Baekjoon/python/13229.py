# source : https://www.acmicpc.net/problem/13229

# input
n = int(input())
array = list(map(int, input().split()))

for _ in range(int(input())):
    # input
    start, end = map(int, input().split())
    
    print(sum(array[start:end + 1]))