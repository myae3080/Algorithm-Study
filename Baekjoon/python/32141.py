# source : https://www.acmicpc.net/problem/32141

def main():
    # input
    N, H = map(int, input().split())
    cards = list(map(int, input().split()))
    
    result = 0
    for c in cards:
        if H > 0:
            result += 1
            H -= c
        else:
            break
    
    print(result if H <= 0 else -1)

if __name__ == '__main__':
    main()