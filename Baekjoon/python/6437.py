# source : https://www.acmicpc.net/problem/6437

def main():
    hole = 0
    while 1:
        # input
        par, shot = map(int, input().split())
        
        if par == 0:
            break
        
        hole += 1
        
        print('Hole #{0}'.format(hole))
        
        if shot == 1:
            print('Hole-in-one.')
        elif par - shot == 3:
            print('Double eagle.')
        elif par - shot == 2:
            print('Eagle.')
        elif par - shot == 1:
            print('Birdie.')
        elif par - shot == 0:
            print('Par.')
        elif shot - par == 1:
            print('Bogey.')
        elif shot - par > 1:
            print('Double Bogey.')
        
        print()

if __name__ == '__main__':
    main()