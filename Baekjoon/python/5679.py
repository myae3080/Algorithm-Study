# source : https://www.acmicpc.net/problem/5679

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        result = n
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            
            result = max(result, n)
        
        print(result)

if __name__ == '__main__':
    main()