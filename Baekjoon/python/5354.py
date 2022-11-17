# source : https://www.acmicpc.net/problem/5354

for _ in range(int(input())):
    # input
    n = int(input())
    
    if n < 3:
        for _ in range(n):
            print('#' * n)
    else:
        for i in range(n):
            if i == 0 or i == (n - 1):
                print('#' * n)
            else:
                print('#' + 'J' * (n - 2) + '#')
    print()