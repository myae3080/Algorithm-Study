# source : https://www.acmicpc.net/problem/7120

def main():
    # input
    s = input()
    
    result = s[0]
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            result += s[i]
    
    print(result)

if __name__ == '__main__':
    main()