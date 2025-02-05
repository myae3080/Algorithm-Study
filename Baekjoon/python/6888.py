# source : https://www.acmicpc.net/problem/6888

def main():
    # input
    X, Y = int(input()), int(input())
    
    for y in range(X, Y + 1, 60):
        print('All positions change in year %d' % y)

if __name__ == '__main__':
    main()