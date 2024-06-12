# source : https://www.acmicpc.net/problem/31833

def main():
    # input
    n = int(input())
    a, b = int(''.join(input().split())), int(''.join(input().split()))
    
    print(min(a, b))

if __name__ == '__main__':
    main()