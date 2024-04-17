# source : https://www.acmicpc.net/problem/25644

def main():
    # input
    n = int(input())
    stock = list(map(int, input().split()))
    
    high_point, result = 0, 0
    for i in range(n - 1, -1, -1):
        high_point = max(high_point, stock[i])
        result = max(result, high_point - stock[i])
    
    print(result)

if __name__ == '__main__':
    main()