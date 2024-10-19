# source : https://www.acmicpc.net/problem/5768

def main():
    while 1:
        # input
        M, N = map(int, input().split())
        
        if M == N == 0:
            break
        
        x, y = 0, 0
        for i in range(M, N + 1):
            count = 0
            
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
                
                if count >= y:
                    x = i
                    y = count
        
        print(x, y)

if __name__ == '__main__':
    main()