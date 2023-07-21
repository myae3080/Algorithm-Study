# source : https://www.acmicpc.net/problem/17502

def main():
    # input
    n = int(input())
    word = list(input())
    
    if word.count('?') == n:
        print('a' * n)
    else:
        half = n // 2
        if half * 2 != n and word[half] == '?':
            word[half] = 'a'
        
        for i in range(half):
            if word[i] == word[n - i - 1] == '?':
                word[i] = word[n - i - 1] = 'a'
            elif word[i] != word[n - i - 1]:
                if word[i] == '?':
                    word[i] = word[n - i - 1]
                if word[n - i - 1] == '?':
                    word[n - i - 1] = word[i]
            
        print(''.join(word))

if __name__ ==  '__main__':
    main()