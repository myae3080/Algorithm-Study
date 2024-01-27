# source : https://www.acmicpc.net/problem/14730

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        c, k = map(int, input().split())
        
        result += (c * k)
    
    print(result)

if __name__ == '__main__':
    main()