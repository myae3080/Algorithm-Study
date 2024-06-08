# source : https://www.acmicpc.net/problem/16953

def main():
    # input
    a, b = map(int, input().split())

    paths = []
    while a != b:
        origin = b

        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        
        if b == origin:
            print(-1)
            return
        else:
            paths.append(b)

    print(len(paths) + 1)

if __name__ == '__main__':
    main()