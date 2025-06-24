# source : https://www.acmicpc.net/problem/1895

def main():
    # input
    R, C = map(int, input().split())
    pixels = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())
    
    result = 0
    r, c = 3, 3
    while r < R + 1:
        for _ in range(C - 2):
            filters = []
            for i in range(r - 3, r):
                filters.extend(pixels[i][c - 3:c])
            
            median = sorted(filters)[4]
            if median >= T:
                result += 1
            
            c += 1
        
        r += 1
        c = 3
    
    print(result)

if __name__ == '__main__':
    main()