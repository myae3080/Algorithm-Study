# source : https://www.acmicpc.net/problem/14682

def main():
    # input
    n = int(input())
    k = int(input())
    
    result = n
    for i in range(1, k + 1):
        result += n * (10 ** i)
    
    print(result)

if __name__ == '__main__':
    main()