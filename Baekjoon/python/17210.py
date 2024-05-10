# source : https://www.acmicpc.net/problem/17210

def main():
    # input
    n, way = int(input()), int(input())

    if n >= 6:
        print('Love is open door')
    else:
        for _ in range(n - 1):
            way ^= 1

            print(way)

if __name__ == '__main__':
    main()