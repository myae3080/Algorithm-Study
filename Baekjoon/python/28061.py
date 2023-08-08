# source : https://www.acmicpc.net/problem/28061

def main():
    # input
    n = int(input())
    max_lemons = [lemon - (n - i) for i, lemon in enumerate(list(map(int, input().split())))]
    
    print(max(max_lemons))

if __name__ == '__main__':
    main()