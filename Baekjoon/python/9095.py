# dynamic programming

# input
count = int(input())

def recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return recursive(n - 3) + recursive(n - 2) + recursive(n - 1)

[print(recursive(int(input()))) for i in range(count)]