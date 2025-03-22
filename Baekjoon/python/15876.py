# source : https://www.acmicpc.net/problem/15876

def main():
    # input
    n, k = map(int, input().split())
    
    result = []
    binary = ''
    for i in range(101):
        binary += bin(i)[2:]
    
    for i in range(5):
        result.append(binary[n * i + (k - 1)])
    
    print(*result)

if __name__ == '__main__':
    main()