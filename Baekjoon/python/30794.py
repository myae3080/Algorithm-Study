# source : https://www.acmicpc.net/problem/30794

def main():
    # input
    n, lv = input().split()

    point_by_lv = {
        'miss': 0
        , 'bad': 200
        , 'cool': 400
        , 'great': 600
        , 'perfect': 1000
    }

    print(int(n) * point_by_lv[lv])

if __name__ == '__main__':
    main()