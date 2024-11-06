# source : https://www.acmicpc.net/problem/5341

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        print((n + 1) * n // 2)

if __name__ == '__main__':
    main()