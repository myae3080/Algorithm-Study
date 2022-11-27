# source : https://www.acmicpc.net/problem/17176

def decoder(n: int) -> str:
    if n == 0:
        return ' '
    elif n >= 1 and n <= 26:
        return chr(n + 96)
    else:
        return chr(n + 38)

# input
N = int(input())
cryptographs = list(map(int, input().split()))
plain = sorted([c.lower() for c in list(input())])

result = sorted([decoder(c).lower() for c in cryptographs])

print('y') if plain == result else print('n')