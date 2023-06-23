# source : https://www.acmicpc.net/problem/22938

def main():
    # input
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())

    center_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if center_distance < (r1 + r2):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()