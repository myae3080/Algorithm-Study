# source : https://www.acmicpc.net/problem/15236

def main():
    # input
    n = int(input())
    
    result = 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            result += (i + j)
    
    print(result)

if __name__ == '__main__':
    main()