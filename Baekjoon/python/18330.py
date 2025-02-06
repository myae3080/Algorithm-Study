# source : https://www.acmicpc.net/problem/18330

def main():
    # input
    n, k = int(input()), int(input())
    
    limit = min(k + 60, n)
    
    print(limit * 1500 + (n - limit) * 3000)

if __name__ == '__main__':
    main()