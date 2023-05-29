# source : https://www.acmicpc.net/problem/2991

def main():
    # input
    a, b, c, d = map(int, input().split())
    time = list(map(int, input().split()))
    
    for t in time:
        attacked_cnt = 0
        if 0 < t % (a + b) <= a:
            attacked_cnt += 1
        if 0 < t % (c + d) <= c:
            attacked_cnt += 1
    
        print(attacked_cnt)
    
if __name__ == '__main__':
    main()