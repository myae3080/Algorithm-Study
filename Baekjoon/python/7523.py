# source : https://www.acmicpc.net/problem/7523

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        a, b = map(int, input().split())
        
        print('Scenario #{0}:'.format(i))
        print(((b) * (b + 1) // 2) - ((a - 1) * (a) // 2))
        print()

if __name__ == '__main__':
    main()