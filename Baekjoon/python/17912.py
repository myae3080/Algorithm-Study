# source : https://www.acmicpc.net/problem/17912

def main():
    # input
    n = int(input())
    days = list(map(int, input().split()))
    
    print(days.index(min(days)))

if __name__ == '__main__':
    main()