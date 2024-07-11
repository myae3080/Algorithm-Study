# source : https://www.acmicpc.net/problem/28135

def main():
    # input
    n = int(input())
    
    result = 0
    for i in range(n):
        result += 1
        
        if '50' in str(i):
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()