# source : https://www.acmicpc.net/problem/11999

def main():
    # input
    X, Y, M = map(int, input().split())
    
    max_x, max_y = M // X, M // Y
    
    result = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            total = i * X + j * Y
            if total > M:
                break
            
            result = max(result, total)
    
    print(result)

if __name__ == '__main__':
    main()