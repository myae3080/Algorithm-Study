# source : https://www.acmicpc.net/problem/1816

def main():
    # input
    for _ in range(int(input())):
        # input
        S = int(input())
        
        is_yes = True
        for n in range(2, 1000001):
            if S % n == 0:
                is_yes = False
                print('NO')
                
                break
                
        if is_yes:
            print('YES')

if __name__ == '__main__':
    main()