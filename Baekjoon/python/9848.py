# source : https://www.acmicpc.net/problem/9848

def main():
    # input
    n, k = map(int, input().split())
    js = [int(input()) for _ in range(n)]
    
    count = 0
    for i in range(n - 1):
        if js[i] - js[i + 1] >= k:
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()