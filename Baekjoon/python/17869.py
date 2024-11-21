# source : https://www.acmicpc.net/problem/17869

def main():
    # input
    n = int(input())
    
    result = 0
    while n != 1:
        n = n + 1 if n % 2 else n // 2
        
        result += 1
    
    print(result)

if __name__ == '__main__':
    main()