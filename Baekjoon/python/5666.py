# source : https://www.acmicpc.net/problem/5666

def main():
    while 1:
        try:
            # input
            H, P = map(int, input().split())
            
            print('{:.2f}'.format(H / P))
        except EOFError:
            break

if __name__ == '__main__':
    main()