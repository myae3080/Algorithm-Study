# source : https://www.acmicpc.net/problem/32288

def main():
    # input
    n = int(input())
    s = input()
    
    result = ''
    for c in s:
        result +=  c.lower() if c.isupper() else c.upper()
    
    print(result)

if __name__ == '__main__':
    main()