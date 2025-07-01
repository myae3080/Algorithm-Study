# source : https://www.acmicpc.net/problem/18242

def main():
    # input
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    
    # UP or DOWN
    is_up = True
    for i in range(N):
        if '#.#' in data[i]:
            if is_up:
                print('UP')
                
                return
            else:
                print('DOWN')
                
                return
        
        if '#' in data[i]:
            is_up = False
    
    # LEFT or RIGHT
    is_left = True
    for i in range(M):
        column = ''.join([data[j][i] for j in range(N)])
        
        if '#.#' in column:
            if is_left:
                print('LEFT')
                
                return
            else:
                print('RIGHT')
                
                return
        
        if '#' in column:
            is_left = False

if __name__ == '__main__':
    main()