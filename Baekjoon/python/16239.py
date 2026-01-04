# source : https://www.acmicpc.net/problem/16239

def main():
    # input
    K, N = int(input()), int(input())

    for i in range(1, N):
        print(i)

        K -= i
    
    print(K)

if __name__ == '__main__':
    main()