# source : https://www.acmicpc.net/problem/34032

def main():
    # input
    N = int(input())
    command = list(input())
     
    base = N // 2 if N % 2 == 0 else N // 2 + 1
    if command.count('O') >= base:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()