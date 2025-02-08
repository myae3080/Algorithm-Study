# source : https://www.acmicpc.net/problem/31229

def main():
    # input
    N = int(input())
    
    print(*[2 * i - 1 for i in range(1, N + 1)])

if __name__ == '__main__':
    main()