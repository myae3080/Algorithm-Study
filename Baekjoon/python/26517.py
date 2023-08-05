# source : https://www.acmicpc.net/problem/26517

def main():
    # input
    k = int(input())
    a, b, c, d = map(int, input().split())
    
    left = a * k + b
    right = c * k + d
    
    print('Yes', left) if left == right else print('No')

if __name__ == '__main__':
    main()