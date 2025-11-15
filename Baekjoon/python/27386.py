# source : https://www.acmicpc.net/problem/27386

def main():
    # input
    letter1, letter2 = input(), input()

    print(''.join(sorted(letter1 + letter2)))

if __name__ == '__main__':
    main()