# source : https://www.acmicpc.net/problem/20410

def main():
    # input
    m, seed, x1, x2 = map(int, input().split())

    for a in range(m):
        for c in range(m):
            check_x1 = (a * seed + c) % m
            if x1 == check_x1:
                if x2 == (a * check_x1 + c) % m:
                    print(a, c)

                    return

if __name__ == '__main__':
    main()