# source : https://www.acmicpc.net/problem/30224

def main():
    # input
    str_num = input()

    if str_num.count('7'):
        if int(str_num) % 7 == 0:
            print(3)
        else:
            print(2)
    else:
        if int(str_num) % 7 == 0:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()