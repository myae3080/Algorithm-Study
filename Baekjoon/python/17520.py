# source : https://www.acmicpc.net/problem/17520

def main():
    # input
    n = int(input())
    
    print((2 ** int((n + 1) / 2)) % 16769023)

if __name__ == '__main__':
    main()