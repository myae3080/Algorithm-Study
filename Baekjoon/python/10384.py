# source : https://www.acmicpc.net/problem/10384

def main():
    # input
    for i in range(1, int(input()) + 1):
        alpha_count = [0] * 26
        
        # input
        sentence = input().lower()
        
        for c in sentence:
            if c.isalpha():
                alpha_count[ord(c) - 97] += 1
        
        pangram_num = min(alpha_count)
        if pangram_num == 0:
            print('Case %d: Not a pangram' % i)
        elif pangram_num == 1:
            print('Case %d: Pangram!' % i)
        elif pangram_num == 2:
            print('Case %d: Double pangram!!' % i)
        elif pangram_num == 3:
            print('Case %d: Triple pangram!!!' % i)

if __name__ == '__main__':
    main()