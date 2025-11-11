# source : https://www.acmicpc.net/problem/31408

def main():
    # input
    N = int(input())
    schedule = list(map(int, input().split()))

    d = {}
    for num in schedule:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    print('NO' if max(d.values()) > (N + 1) // 2 else 'YES')

if __name__ == '__main__':
    main()