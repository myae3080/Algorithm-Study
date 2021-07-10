# binary number

for i in range(int(input())):
    # input
    print(bin(sum([int(s, 2) for s in input().split()]))[2:])