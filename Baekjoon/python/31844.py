# source : https://www.acmicpc.net/problem/31844

def main():
    # input
    warehouse = list(input())

    # '.' : 빈 칸 / '@' : 로봇 / '#' : 박스 / '!' : 박스를 놓아야 할 칸
    robot = warehouse.index('@')
    box = warehouse.index('#')
    point = warehouse.index('!')
    
    if (robot < box < point) or (point < box < robot):
        print(abs(point - robot) - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()