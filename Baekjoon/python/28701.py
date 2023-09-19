# source : https://www.acmicpc.net/problem/28701
# sigma

def main():
    # input
    n = int(input())
    
    sum = (n * (n + 1)) // 2
    print(sum)
    print(sum ** 2)
    print(((n * (n + 1)) // 2) ** 2)

if __name__ == '__main__':
    main()