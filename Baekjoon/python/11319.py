# source : https://www.acmicpc.net/problem/11319

def main():
    # input
    for _ in range(int(input())):
        chars = ''
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        # input
        for word in input().split():
            for c in word:
                chars += c.lower()
        
        vowel_cnt = 0
        for c in chars:
            if c in vowels:
                vowel_cnt += 1
        
        print(len(chars) - vowel_cnt, vowel_cnt)

if __name__ == '__main__':
    main()