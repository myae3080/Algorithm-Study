# source : https://www.acmicpc.net/problem/16208

def main():
    # input
    n = int(input())
    rods = list(map(int, input().split()))
    
    total = sum(rods)
    result = 0
    for i in range(n - 1):
        total -= rods[i]
        result += rods[i] * total
    
    print(result)

if __name__ == '__main__':
    main()