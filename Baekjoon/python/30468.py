# source : https://www.acmicpc.net/problem/30468

def main():
    # input
    s, d, i, l, n = map(int, input().split())
    
    print(4 * n - (s + d + i + l) if 4 * n >= (s + d + i + l) else 0)

if __name__ == '__main__':
    main()