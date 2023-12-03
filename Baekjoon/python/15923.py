# source : https://www.acmicpc.net/problem/15923

def main():
    x, y = [], []
    
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        x.append(a)
        y.append(b)
    
    print((max(x) - min(x) + max(y) - min(y)) * 2)

if __name__ == '__main__':
    main()