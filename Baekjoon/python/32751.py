# source : https://www.acmicpc.net/problem/32751

def main():
    # input
    N = int(input())
    ingredients = list(map(int, input().split()))
    S = input()

    if S[0] != 'a' or S[-1] != 'a':
        print('No')
    
        return

    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print('No')

            return
    
    for i in range(4):
        if S.count(chr(i + 97)) > ingredients[i]:
            print('No')
            
            return
    
    print('Yes')

if __name__ == '__main__':
    main()