# source : https://www.acmicpc.net/problem/27512

def main():
    # input
    n, m = map(int, input().split())
    
    if n % 2 == 1 and m % 2 == 1:
        print(n * m - 1)
    else:
        print(n * m)

if __name__ == '__main__':
    main()