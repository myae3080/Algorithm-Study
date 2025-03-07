# source : https://www.acmicpc.net/problem/25183

def main():
    # input
    N = int(input())
    S = input()
    
    for i in range(N - 1):
        lotto = 1
        next_idx = i + 1
        while 1:
            if ord(S[next_idx]) == ord(S[next_idx - 1]) - 1 or ord(S[next_idx]) == ord(S[next_idx - 1]) + 1:
                next_idx += 1
                lotto += 1
                
                if lotto == 5:
                    break
            else:
                break
        
        if lotto == 5:
            print('YES')
            
            return
    
    print('NO')

if __name__ == '__main__':
    main()