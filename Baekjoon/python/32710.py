# source : https://www.acmicpc.net/problem/32710

def main():
    # input
    N = int(input())
    
    for i in range(2, 10):
        for j in range(1, 10):
            if i == N or j == N or (i * j) == N:
                print(1)
                
                return
    
    print(0)

if __name__ == '__main__':
    main()