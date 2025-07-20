# source : https://www.acmicpc.net/problem/25176

def main():
    # input
    N = int(input())
    
    result = 1
    for i in range(1, N + 1):
        result *= i
    
    print(result)

if __name__ == '__main__':
    main()