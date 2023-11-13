# source : https://www.acmicpc.net/problem/2921

def main():
    # input
    n = int(input())
    
    result = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            result += (i + j)
    
    print(result)

if __name__ == '__main__':
    main()