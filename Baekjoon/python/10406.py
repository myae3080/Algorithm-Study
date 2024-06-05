# source : https://www.acmicpc.net/problem/10406

def main():
    # input
    w, n, p = map(int, input().split())
    heights = list(map(int, input().split()))

    result = 0
    for h in heights:
        if w <= h <= n:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()