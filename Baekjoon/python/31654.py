# source : https://www.acmicpc.net/problem/31654

def main():
    # input
    A, B, C = map(int, input().split())

    print('correct!' if A + B == C else 'wrong!')

if __name__ == '__main__':
    main()