# source : https://www.acmicpc.net/problem/26217

def main():
    # input
    n = int(input())

    result = 0
    for i in range(1, n + 1):
        result += (n / i)
    
    print(result)

if __name__ == '__main__':
    main()