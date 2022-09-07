# source : https://www.acmicpc.net/problem/3028

# input
rules = input()

cups = [1, 0, 0]

for rule in rules:
    if rule == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif rule == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]
        
print(cups.index(1) + 1)