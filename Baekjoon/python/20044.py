# source : https://www.acmicpc.net/problem/20044

def main():
    # input
    n = int(input())
    performances = sorted(list(map(int, input().split())))

    result = 200001
    for i in range(n):
        result = min(result, performances[i] + performances[2 * n - i - 1])
    
    print(result)

if __name__ == '__main__':
    main()