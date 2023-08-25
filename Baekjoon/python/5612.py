# source : https://www.acmicpc.net/problem/5612

def main():
    # input
    n, m = int(input()), int(input())
    tunnel_infos = [list(map(int, input().split())) for _ in range(n)]
    
    result = m
    for li in tunnel_infos:
        m = m + li[0] - li[1]
        if m < 0:
            result = 0
            break
        
        result = max(result, m)
    
    print(result)
    
if __name__ == '__main__':
    main()