# https://www.acmicpc.net/problem/18795

def main():
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(sum(A) + sum(B))

if __name__ == '__main__':
    main()