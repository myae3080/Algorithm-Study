# source : https://www.acmicpc.net/problem/16172

def main():
    # input
    s, k = input(), input()
    
    print(1) if ''.join([c for c in s if c.isalpha()]).count(k) else print(0)
    
if __name__ == '__main__':
    main()