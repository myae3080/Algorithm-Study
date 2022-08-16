# source : https://www.acmicpc.net/problem/11966

# input
n = int(input())

squares = [2 ** i for i in range(31)]

print(squares.count(n))