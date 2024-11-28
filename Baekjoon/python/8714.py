# source : https://www.acmicpc.net/problem/8714

def main():
    # input
    n = int(input())
    coins = list(map(int, input().split()))
    
    print(min(coins.count(0), coins.count(1)))

if __name__ == '__main__':
    main()