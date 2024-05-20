# source : https://www.acmicpc.net/problem/8370

def main():
    # input
    n1, k1, n2, k2 = map(int, input().split())
    
    print(n1 * k1 + n2 * k2)

if __name__ == '__main__':
    main()