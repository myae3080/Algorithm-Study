# source : https://www.acmicpc.net/problem/25904

def main():
    # input
    n, x = map(int, input().split())
    upper_limits = list(map(int, input().split()))
    
    is_end = False
    while not is_end:
        for i in range(n):
            if upper_limits[i] < x:
                is_end = True
                result = i + 1
                break
            else:
                x += 1
    
    print(result)

if __name__ == '__main__':
    main()