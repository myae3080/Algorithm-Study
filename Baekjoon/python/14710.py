# source : https://www.acmicpc.net/problem/14710

def main():
    # input
    angle1, angle2 = map(int, input().split())

    if (angle1 % 30) * 12 == angle2:
        print('O')
    else:
        print('X')

if __name__ == '__main__':
    main()