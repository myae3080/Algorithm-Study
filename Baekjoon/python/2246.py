# source : https://www.acmicpc.net/problem/2246

def main():
    # input
    condos = sorted([list(map(int, input().split())) for _ in range(int(input()))])
    
    cost, result = 10001, 0
    for condo in condos:
        if condo[1] < cost:
            result += 1
            cost = condo[1]
    
    print(result)

if __name__ == '__main__':
    main()