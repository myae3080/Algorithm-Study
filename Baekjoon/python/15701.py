# source : https://www.acmicpc.net/problem/15701

def main():
    # input
    n = int(input())
    
    result = 0
    for i in range(1, int(n ** 0.5) + 1):
        if i * i == n:
            result += 1
        else:
            if n % i == 0:
                result += 2

    print(result)

if __name__ == '__main__':
    main()