# source : https://www.acmicpc.net/problem/20115

def main():
    # input
    N = int(input())
    drinks = sorted(list(map(int, input().split())))

    total = drinks[-1]
    total += sum([drinks[i] / 2 for i in range(N - 1)])

    print(total)

if __name__ == '__main__':
    main()