# source : https://www.acmicpc.net/problem/16189

def main():
    # input
    s = input()
    k = int(input())
    
    s_size = len(s)
    for i in range(s_size // 2):
        if s[i] != s[s_size - i - 1]:
            print('NO')
            
            return
    
    print('YES')
    
if __name__ == '__main__':
    main()