# source : https://www.acmicpc.net/problem/14219

def main():
    # input
    n, m = map(int, input().split())
    
    print('YES' if (n * m) % 3 == 0 else 'NO')

if __name__ == '__main__':
    main()