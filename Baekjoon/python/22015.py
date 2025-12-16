# source : https://www.acmicpc.net/problem/22015

def main():
    # input
    candies = list(map(int, input().split()))

    max_val = max(candies)

    result = 0
    for c in candies:
        result += max_val - c
    
    print(result)

if __name__ == '__main__':
    main()