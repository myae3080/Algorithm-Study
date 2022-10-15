# source : https://www.acmicpc.net/problem/16968

# input
number = input()

format = {
    'd': 10,
    'c': 26
}

prev = ''
result = 1
for s in number:
    if prev == s:
        result *= (format[s] - 1)
    else:
        result *= format[s]
        
    prev = s

print(result)