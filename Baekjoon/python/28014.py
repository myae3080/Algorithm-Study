# source : https://www.acmicpc.net/problem/28014

def main():
    # input
    n = int(input())
    towers = list(map(int, input().split()))
    
    result = 1
    for i in range(1, n):
        if towers[i - 1] <= towers[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()