# source : https://www.acmicpc.net/problem/25991

def main():
    # input
    n = int(input())
    nums = list(map(float, input().split()))
    
    total_volume = 0
    for num in nums:
        total_volume += num ** 3
    
    print(total_volume ** (1/3))

if __name__ == '__main__':
    main()