# star

# input
line = int(input())

for i in range(1, line + 1):
    print(" " * (line - i) + "*" * (2 * i - 1))