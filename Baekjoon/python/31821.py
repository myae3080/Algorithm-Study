# source : https://www.acmicpc.net/problem/31821

def main():
    # input
    n = int(input())
    menu = [int(input()) for _ in range(n)]
    m = int(input())
    newbie = [int(input()) for _ in range(m)]
    
    print(sum([menu[i - 1] for i in newbie]))

if __name__ == '__main__':
    main()