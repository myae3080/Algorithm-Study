# source : https://www.acmicpc.net/problem/9550

def main():
    for _ in range(int(input())):
        # input
        n, k = map(int, input().split())
        candies = list(map(int, input().split()))
    
        result = 0
        for candy in candies:
            result += (candy // k)
        
        print(result)

if __name__ == '__main__':
    main()