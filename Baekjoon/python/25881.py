# source : https://www.acmicpc.net/problem/25881

def main():
    # input
    first, additional = map(int, input().split())
    
    # inpu
    for _ in range(int(input())):
        # input
        n = int(input())
        
        if n <= 1000:
            print(n, n * first)
        else:
            print(n, 1000 * first + (n - 1000) * additional)

if __name__ == '__main__':
    main()