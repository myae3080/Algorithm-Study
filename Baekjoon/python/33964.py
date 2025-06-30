# source : https://www.acmicpc.net/problem/33964

def main():
    # input
    X, Y = map(int, input().split())
    
    print('1' * abs(X - Y) + '2' * min(X, Y))

if __name__ == '__main__':
    main()