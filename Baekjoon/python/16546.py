# source : https://www.acmicpc.net/problem/16546

def main():
    # input
    n = int(input())
    runners = list(map(int, input().split()))
    
    print((n * (n + 1) // 2) - sum(runners))

if __name__ == '__main__':
    main()