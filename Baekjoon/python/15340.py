# source : https://www.acmicpc.net/problem/15340

def main():
    while 1:
        # input
        c, d = map(int, input().split())
        
        if c == d == 0:
            break
        
        print(min(c * 30 + d * 40, c * 35 + d * 30, c * 40 + d * 20))

if __name__ == '__main__':
    main()