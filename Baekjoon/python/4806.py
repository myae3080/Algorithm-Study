# source : https://www.acmicpc.net/problem/4806

result = 0
while True:
    try:
        # input
        input()
        result += 1
    except EOFError:
        break

print(result)