# source : https://www.acmicpc.net/problem/16673

def main():
    # input
    c, k, p = map(int, input().split())
    
    result = 0
    for n in range(1, c + 1):
        result += (k * n) + (p * (n ** 2))
    
    print(result)

    
if __name__ == '__main__':
    main()