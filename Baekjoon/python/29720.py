# source : https://www.acmicpc.net/problem/29720

def main():
    # input
    n, m, k = map(int, input().split())
    
    minimum = n - (m * k) if n >= (m * k) else 0
    maximum = n - (m * (k - 1)) - 1
    
    print(minimum, maximum)

if __name__ == '__main__':
    main() 