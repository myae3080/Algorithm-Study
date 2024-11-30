# source : https://www.acmicpc.net/problem/20112

def main():
    # input
    N = int(input())
    squares = [list(input()) for _ in range(N)]
    
    for i in range(N):
        compare1 = squares[i]
        
        compare2 = ''
        for j in range(N):
            compare2 += squares[j][i]
        
        if ''.join(compare1) != compare2:
            print('NO')
            return
    
    print('YES')

if __name__ == '__main__':
    main()