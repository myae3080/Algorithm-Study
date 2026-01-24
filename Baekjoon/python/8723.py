# source : https://www.acmicpc.net/problem/8723

def main():
    # input
    sides = sorted(list(map(int, input().split())))

    if len(set(sides)) == 1:
        print(2)
    elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()