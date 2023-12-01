# source : https://www.acmicpc.net/problem/29736

def main():
    # input
    a, b = map(int, input().split())
    k, x = map(int, input().split())
    
    result = 0
    for q in range(k - x, k + x + 1):
        if a <= q <= b:
            result += 1
    
    print('IMPOSSIBLE' if result == 0 else result)

if __name__ == '__main__':
    main()