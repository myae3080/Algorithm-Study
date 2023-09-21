# source : https://www.acmicpc.net/problem/1531

def main():
    pictures = [[0] * 100 for _ in range(100)]
    
    # input
    n, m = map(int, input().split())
    
    for _ in range(n):
        # input
        lx, ly, rx, ry = map(int, input().split())
        
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                pictures[x - 1][y - 1] += 1
                
    result = 0
    for i in range(100):
        for j in range(100):
            if pictures[i][j] > m:
                result += 1

    print(result)

if __name__ == '__main__':
    main()