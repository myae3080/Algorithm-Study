# source : https://www.acmicpc.net/problem/26509

def main():
    # input
    for _ in range(int(input())):
        # input
        first = sorted(list(map(int, input().split())), reverse=True)
        second = sorted(list(map(int, input().split())), reverse=True)

        if first != second:
            print('NO')

            continue

        if first[0] ** 2 != (first[1] ** 2 + first[2] ** 2):
            print('NO')

            continue

        if second[0] ** 2 != (second[1] ** 2 + second[2] ** 2):
            print('NO')
        
            continue
        
        print('YES')

if __name__ == '__main__':
    main()