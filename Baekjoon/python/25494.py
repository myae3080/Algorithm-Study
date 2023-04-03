# source : https://www.acmicpc.net/problem/25494

def main():
    # input
    t = int(input())
    for _ in range(t):
        # input
        case = list(map(int, input().split()))
        
        print(min(case))
        
if __name__ == '__main__':
    main()