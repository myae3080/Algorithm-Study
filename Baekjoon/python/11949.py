# source : https://www.acmicpc.net/problem/11949

def main():
    # input
    N, M = map(int, input().split())
    cards = [int(input()) for _ in range(N)]
    
    for i in range(1, M + 1):
        for j in range(N - 1):
            if (cards[j] % i) > (cards[j + 1] % i):
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
    
    for card in cards:
        print(card)

if __name__ == '__main__':
    main()