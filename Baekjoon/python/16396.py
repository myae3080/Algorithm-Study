# source : https://www.acmicpc.net/problem/16396

def main():
    points = [0] * 10001
    max_x = 0
    
    # input
    for _ in range(int(input())):
        # input
        x, y = map(int, input().split())
        
        for i in range(x, y):
            if points[i] != 1:
                points[i] = 1
        
        max_x = max(y, max_x)
        
    print(sum(points[:max_x]))

if __name__ == '__main__':
    main()