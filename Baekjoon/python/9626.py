# source : https://www.acmicpc.net/problem/9626

def main():
    # input
    M, N = map(int, input().split())
    U, L, R, D = map(int, input().split())
    words = [input() for _ in range(M)]
    
    word_cnt = M
    u = U
    for r in range(M + U + D):
        row = ''
        start = '#' if r % 2 == 1 else '.'
        if u > 0:
            u -= 1
            for j in range(N + L + R):
                if start == '#':
                    row += '#' if j % 2 == 1 else '.'
                else:
                    row += '.' if j % 2 == 1 else '#'
        else:
            for j in range(N + L + R):
                if word_cnt > 0 and L <= j < N + L:
                    row += words[M - word_cnt][j - L]
                else:
                    if start == '#':
                        row += '#' if j % 2 == 1 else '.'
                    else:
                        row += '.' if j % 2 == 1 else '#'
            
            word_cnt -= 1

        print(row)

if __name__ == '__main__':
    main()