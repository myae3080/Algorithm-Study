# source : https://www.acmicpc.net/problem/17174

def main():
    # input
    n, m = map(int, input().split())
    
    result = n
    
    while n > 0:
        n //= m
        result += n

    print(result)

if __name__ == '__main__':
    main()