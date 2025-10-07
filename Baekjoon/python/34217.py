# source : https://www.acmicpc.net/problem/34217

def main():
    # input
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    if A + C < B + D:
        print('Hanyang Univ.')
    elif A + C > B + D:
        print('Yongdap')
    else:
        print('Either')

if __name__ == '__main__':
    main()