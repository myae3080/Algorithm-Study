# source : https://www.acmicpc.net/problem/30329

def main():
    # input
    s = input()

    result = 0
    for i in range(len(s)):
        if s[i] == 'k' and s[i:i + 4] == 'kick':
            result += 1
        else:
            continue
    
    print(result)

if __name__ == '__main__':
    main()