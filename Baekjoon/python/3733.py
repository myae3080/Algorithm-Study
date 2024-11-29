# source : https://www.acmicpc.net/problem/3733

def main():
    while 1:
        try:
            # input
            N, S = map(int, input().split())
            
            print(S // (N + 1))
        except EOFError:
            break

if __name__ == '__main__':
    main()