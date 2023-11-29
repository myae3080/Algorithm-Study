# source : https://www.acmicpc.net/problem/2847

def main():
    # input
    n = int(input())
    levels = [int(input()) for _ in range(n)]

    result = 0
    for i in range(n - 2, -1 , -1):
        if levels[i] >= levels[i + 1]:
            down_level = levels[i] - levels[i + 1] + 1
            result += down_level
            levels[i] -= down_level
    
    print(result)

if __name__ == '__main__':
    main()