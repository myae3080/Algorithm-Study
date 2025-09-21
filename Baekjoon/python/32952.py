# source : https://www.acmicpc.net/problem/32952

def main():
    # input
    R, K, M = map(int, input().split())

    r = M // K
    while r > 0 and R > 0:
        r -= 1
        R //= 2
    
    print(R)

if __name__ == '__main__':
    main()