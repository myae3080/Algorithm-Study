# source : https://www.acmicpc.net/problem/32401

def main():
    # input
    N = int(input())
    S = input()

    result = 0
    for i in range(N):
        if S[i] == 'A':
            for j in range(i + 1, N):
                if S[j] == 'A':
                    n_cnt = S[i:j + 1].count('N')
                    if n_cnt == 1:
                        result += 1

                    break
    
    print(result)

if __name__ == '__main__':
    main()