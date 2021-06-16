# math

for i in range(int(input())):
    # input
    h, w, n = map(int, input().split())

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            n -= 1
            if n == 0:
                print(str(j) + (str(i) if i >= 10 else '0' + str(i)))