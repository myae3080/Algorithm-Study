# source : https://www.acmicpc.net/problem/27434

# PyPy3

def main():
    # input
    n = int(input())

    if n == 0:
        print(1)
    else:
        result = 1
        for i in range(n, 1, -1):
            result *= i
        
        print(result)
    
if __name__ == '__main__':
    main()