# source : https://www.acmicpc.net/problem/15751

def main():
    # input
    a, b, x, y = map(int, input().split())
    
    print(min(abs(a - b), abs(max(a, b) - max(x, y)) + abs(min(a, b) - min(x, y))))

if __name__ == '__main__':
    main()