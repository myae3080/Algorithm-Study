# source : https://www.acmicpc.net/problem/2605

# input
n = int(input())
numbers = list(map(int, input().split()))

line = []
[line.insert(i - numbers[i], i + 1) for i in range(n)]
    
[print(student, end=' ') for student in line]