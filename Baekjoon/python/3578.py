# source : https://www.acmicpc.net/problem/3578

def main():
    # input
    h = int(input())

    if h == 0:
        print(1)
    elif h == 1:
        print(0)
    else:
        print('4' * (h % 2) + '8' * (h // 2))

if __name__ == '__main__':
    main()