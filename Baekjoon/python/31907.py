# source : https://www.acmicpc.net/problem/31907

def main():
    # input
    K = int(input())

    print_li = [
        'G' * K + '.' * K * 3
        , '.' * K + 'I' * K + '.' * K + 'T' * K
        , '.' * K * 2 + 'S' * K + '.' * K
    ]

    for s in print_li:
        for _ in range(K):
            print(s)

if __name__ == '__main__':
    main()