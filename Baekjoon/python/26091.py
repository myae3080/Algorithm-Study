# source : https://www.acmicpc.net/problem/26091

def main():
    # input
    N, M = map(int, input().split())
    members = list(map(int, input().split()))

    if N < 2:
        print(0)

        return

    members.sort()
    
    result = 0
    left, right = 0, N - 1
    while left < right:
        if members[left] + members[right] >= M:
            result += 1
            left += 1
            right -= 1
        else:
            left += 1
    
    print(result)

if __name__ == '__main__':
    main()