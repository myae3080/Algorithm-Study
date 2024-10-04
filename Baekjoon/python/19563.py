# source : https://www.acmicpc.net/problem/19563

def main():
    # input
    a, b, c = map(int, input().split())
    
    sum_coordinate = abs(a) + abs(b)
    
    if sum_coordinate <= c:
        if c % 2 == 0:
            print('YES' if sum_coordinate % 2 == 0 else 'NO')
        else:
            print('YES' if sum_coordinate % 2 == 1 else 'NO')
    else:
        print('NO')

if __name__ == '__main__':
    main()