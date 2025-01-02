# source : https://www.acmicpc.net/problem/11758

def main():
    # input
    points = [list(map(int, input().split())) for _ in range(3)]
    
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    
    if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
        print(0)
    elif (y3 - y1) * (x2 - x1) < (y2 - y1) * (x3 - x1):
        print(-1)
    else:
        print(1)

if __name__ == '__main__':
    main()