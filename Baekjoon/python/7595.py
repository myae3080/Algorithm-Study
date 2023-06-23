# source : https://www.acmicpc.net/problem/7595

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        [print('*' * i) for i in range(1, n + 1)]
            
if __name__ == '__main__':
    main()