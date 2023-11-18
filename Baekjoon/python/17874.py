# source : https://www.acmicpc.net/problem/17874

def main():
    # input
    n, h, v = map(int, input().split())
    
    piece = max(h, n - h) * max(v, n - v)
    
    print(piece * 4)

if __name__ == '__main__':
    main()