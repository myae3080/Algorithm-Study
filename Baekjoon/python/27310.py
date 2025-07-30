# source : https://www.acmicpc.net/problem/27310

def main():
    # input
    imoji = input()

    print(len(imoji) + imoji.count(':') + imoji.count('_') * 5)

if __name__ == '__main__':
    main()