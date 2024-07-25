# source : https://www.acmicpc.net/problem/31669

def main():
    # input
    N, M = map(int, input().split())
    schedule = [list(input()) for _ in range(N)]
    
    is_not_possible = True
    for i in range(M):
        teacher = 0
        
        for j in range(N):
            if schedule[j][i] == 'O':
                teacher += 1
                break
        
        if teacher == 0:
            print(i + 1)
            is_not_possible = False
            break
    
    if is_not_possible:
        print('ESCAPE FAILED')

if __name__ == '__main__':
    main()