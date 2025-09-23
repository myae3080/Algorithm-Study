# source : https://www.acmicpc.net/problem/2491

def main():
    # input
    N = int(input())
    arr = list(map(int, input().split()))

    length = 1
    max_length = 1
    for i in range(1, N):
        if arr[i - 1] <= arr[i]:
            length += 1
        else:
            length = 1

        max_length = max(max_length, length)
    
    length = 1
    for i in range(1, N):
        if arr[i - 1] >= arr[i]:
            length += 1
        else:
            length = 1

        max_length = max(max_length, length)
    
    print(max_length)

if __name__ == '__main__':
    main()