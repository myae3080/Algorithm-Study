# source : https://www.acmicpc.net/problem/5073
# geometry

while True:
    # input
    sides = sorted(list(map(int, input().split())))

    if sum(sides) == 0:
        break

    if sides[2] >= sum(sides[:2]):
        print("Invalid")
    else:
        if sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[0] != sides[1] != sides[2]:
            print("Scalene")
        else:
            print("Isosceles")