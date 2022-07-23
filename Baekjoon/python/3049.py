# source : https://www.acmicpc.net/problem/3049

def solution1():
    # input
    n = int(input())
    
    print(n * (n - 1) * (n - 2) * (n - 3) // 24)
    
solution1()