# source : https://www.acmicpc.net/problem/27433

def main():
    # input
    n = int(input())
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
        
    print(result)
    
if __name__ == '__main__':
    main()