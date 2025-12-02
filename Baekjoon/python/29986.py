# source : https://www.acmicpc.net/problem/29986

def main():
    # input
    N, H = map(int, input().split())
    required_heights = list(map(int, input().split()))

    result = 0
    for h in required_heights:
        if H >= h:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()