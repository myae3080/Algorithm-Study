# source : https://www.acmicpc.net/problem/25915

def main():
    # input
    alpha = input()
    
    yonsei = 'ILOVEYONSEI'
    
    result = 0
    for c in yonsei:
        result += abs(ord(c) - ord(alpha))
        alpha = c
    
    print(result)

if __name__ == '__main__':
    main()