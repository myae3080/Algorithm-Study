# source : https://www.acmicpc.net/problem/15818

def main():
    # input
    n, m = map(int, input().split())
    integers = list(map(int, input().split()))
    
    result = 1
    for i in integers:
        result *= (i % m)
    
    print(result % m)

if __name__ == '__main__':
    main()