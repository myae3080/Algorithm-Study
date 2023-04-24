# source : https://www.acmicpc.net/problem/27159

def main():
    # input
    n = int(input())
    cards = list(map(int, input().split()))
    
    result = cards[0]
    for i in range(1, n):
        if cards[i] - cards[i - 1] != 1:
            result += cards[i]
    
    print(result)
    
if __name__ == '__main__':
    main()