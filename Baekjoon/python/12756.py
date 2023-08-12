# source : https://www.acmicpc.net/problem/12756

def main():
    # input
    a1, l1 = map(int, input().split())
    a2, l2 = map(int, input().split())
    
    while 1:
        l1 = max(0, l1 - a2)
        l2 = max(0, l2 - a1)
        
        if l1 == l2 == 0:
            print('DRAW')
            break
        elif l1 == 0:
            print('PLAYER B')
            break
        elif l2 == 0:
            print('PLAYER A')
            break
            
if __name__ == '__main__':
    main()