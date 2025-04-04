# source : https://www.acmicpc.net/problem/11121

def main():
    # input
    for _ in range(int(input())):
        # input
        t1, t2 = input().split()
        
        if t1 == t2:
            print('OK')
        else:
            print('ERROR')

if __name__ == '__main__':
    main()