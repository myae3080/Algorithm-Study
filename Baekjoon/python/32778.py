# source : https://www.acmicpc.net/problem/32778

def main():
    # input
    name = input()

    if name.count('(') == 0:
        print(name)
        print('-')
    else:
        main, sub = name.split('(')
        sub = sub.replace(')', '')

        print(main)
        print(sub)

if __name__ == '__main__':
    main()