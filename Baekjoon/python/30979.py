# source : https://www.acmicpc.net/problem/30979

def main():
    # input
    t = int(input())
    n = int(input())
    tastes = list(map(int, input().split()))

    print('Padaeng_i Happy' if sum(tastes) >= t else 'Padaeng_i Cry')

if __name__ == '__main__':
    main()