# source : https://www.acmicpc.net/problem/34071

def main():
    # input
    N = int(input())
    difficulties = [int(input()) for _ in range(N)]

    if difficulties[0] == max(difficulties):
        print('hard')
    elif difficulties[0] == min(difficulties):
        print('ez')
    else:
        print('?')

if __name__ == '__main__':
    main()