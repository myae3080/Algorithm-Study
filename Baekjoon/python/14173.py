# source : https://www.acmicpc.net/problem/14173

def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    x = [x1, x2, x3, x4]
    y = [y1, y2, y3, y4]
    
    width = max(x) - min(x)
    height = max(y) - min(y)
    
    print(width ** 2) if width > height else print(height ** 2)
    
if __name__ == '__main__':
    main()