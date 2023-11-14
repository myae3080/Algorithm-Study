# source : https://www.acmicpc.net/problem/5724

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
            
        print(sum([i ** 2 for i in range(1, n + 1)]))

if __name__ == '__main__':
    main()