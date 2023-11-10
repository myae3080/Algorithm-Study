# source : https://www.acmicpc.net/problem/28352

def main():
    # input
    n = int(input())
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    print(result // (7 * 24 * 3600))

if __name__ == '__main__':
    main()