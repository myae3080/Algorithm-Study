# source : https://www.acmicpc.net/problem/21965

def main():
    # input
    N = int(input())
    seq = list(map(int, input().split()))

    is_mountain = True
    is_up = True
    for i in range(1, N):
        if seq[i - 1] == seq[i]:
            is_mountain = False

            break
        
        if is_up:
            if seq[i - 1] > seq[i]:
                is_up = False
        else:
            if seq[i - 1] < seq[i]:
                is_mountain = False
    
    print('YES' if is_mountain else 'NO')

if __name__ == '__main__':
    main()