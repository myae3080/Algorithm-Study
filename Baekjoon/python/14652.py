# source : https://www.acmicpc.net/problem/14652

def main():
    # input
    n, m, k = map(int, input().split())
    
    print(k // m, k % m)
    
if __name__ == '__main__':
    main()