# source : https://www.acmicpc.net/problem/11908

def main():
    # input
    n = int(input())
    cards = sorted(list(map(int, input().split())))
    
    print(sum(cards[:n - 1]))

if __name__ == '__main__':
    main()