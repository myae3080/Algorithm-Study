# source : https://www.acmicpc.net/problem/3135

def main():
    # input
    a, b = map(int, input().split())
    bookmarks = [int(input()) for _ in range(int(input()))]
    
    curr_hz = a
    for f in bookmarks:
        if abs(curr_hz -b) > abs(f - b):
            curr_hz = f
    
    result = 0
    if a != curr_hz:
        result += 1
    
    result += abs(curr_hz - b)

    print(result)

if __name__ == '__main__':
    main()