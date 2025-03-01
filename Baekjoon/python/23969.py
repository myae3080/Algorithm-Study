# source : https://www.acmicpc.net/problem/23969

# PyPy3

def main():
    # input
    N, K = map(int, input().split())
    array = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                K -= 1
            
            if K == 0:
                print(*array)
                
                return
    
    print(-1)

if __name__ == '__main__':
    main()