# source : https://www.acmicpc.net/problem/

def main():
    # input
    n = int(input())
    s = input()
    
    chars = {}
    targets = 'uospc'
    for c in targets:
        chars[c] = 0
    
    for c in s:
        if c in targets:
            chars[c] += 1
    
    print(min(chars.values()))

if __name__ == '__main__':
    main()