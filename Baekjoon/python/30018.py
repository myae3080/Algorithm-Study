# source : https://www.acmicpc.net/problem/30018

def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = 0
    for i in range(n):
        result += abs(a[i] - b[i])
    
    print(result // 2)

if __name__ == '__main__':
    main()