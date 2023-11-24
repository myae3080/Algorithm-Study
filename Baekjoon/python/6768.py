# source : https://www.acmicpc.net/problem/6768

def main():
    # input
    n = int(input())
    
    print((n - 3) * (n - 2) * (n - 1) // 6)

if __name__ == '__main__':
    main()