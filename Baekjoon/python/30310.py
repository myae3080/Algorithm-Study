# source : https://www.acmicpc.net/problem/30310

def main():
    # input
    n = int(input())
    forks = sorted(list(map(int, input().split())))
    
    print(forks[0] + forks[1])

if __name__ == '__main__':
    main()