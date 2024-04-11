# source : https://www.acmicpc.net/problem/18856

def main():
    # input
    n = int(input())
    
    result = [0 for _ in range(n)]
    result[0], result[1], result[-1] = 1, 2, 997
    
    for i in range(2, n - 1):
        result[i] = result[i - 1] + 1
    
    print(n)
    for num in result:
        print(num, end=' ')

if __name__ == '__main__':
    main()