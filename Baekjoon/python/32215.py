# source : https://www.acmicpc.net/problem/32215

def main():
    # input
    n, m, k = map(int, input().split())
    
    print(m * k + m)

if __name__ == '__main__':
    main()