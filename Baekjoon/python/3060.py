# source : https://www.acmicpc.net/problem/3060

def main():
    # input
    for _ in range(int(input())):
        # input
        N = int(input())
        feedstuff = list(map(int, input().split()))
        
        result = 1
        feedstuff_sum = sum(feedstuff)
        while N >= feedstuff_sum:
            result += 1
            feedstuff_sum *= 4
        
        print(result)

if __name__ == '__main__':
    main()