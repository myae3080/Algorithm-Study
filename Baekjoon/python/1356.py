# source : https://www.acmicpc.net/problem/1356
# math, string

# input
n = input()

is_false = True

for i in range(1, len(n)):
    str_a, str_b = n[:i], n[i:]
    int_a, int_b = 1, 1

    for s in str_a:
        int_a *= int(s)

    for s in str_b:
        int_b *= int(s)

    if int_a == int_b:
        print('YES')
        is_false = False
        break

if is_false:
    print('NO')