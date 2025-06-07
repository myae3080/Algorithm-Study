# source : https://www.acmicpc.net/problem/15184

def main():
    # input
    text = input().upper()

    chars_count = [0] * 26
    for c in text:
        if c.isalpha():
            chars_count[ord(c) - 65] += 1
    
    for i in range(26):
        print(chr(i + 65), '|', '*' * chars_count[i])

if __name__ == '__main__':
    main()