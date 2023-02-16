# source : https://www.acmicpc.net/problem/15781

def main():
    # input
    n, m = map(int, input().split())
    helmets = list(map(int, input().split()))
    vests = list(map(int, input().split()))
    
    print(max(helmets) + max(vests))
    
if __name__ == '__main__':
    main()