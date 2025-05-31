# source : https://www.acmicpc.net/problem/11576

def main():
    # input
    A, B = map(int, input().split())
    m = int(input())
    nums = list(map(int, input().split()))[::-1]
    
    n = 0
    for i in range(m):
        n += nums[i] * (A ** i)
    
    result = []
    while n > 0:
        result.append(n % B)
        n //= B
    
    print(*result[::-1])

if __name__ == '__main__':
    main()