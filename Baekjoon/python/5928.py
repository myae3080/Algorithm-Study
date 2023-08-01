# source : https://www.acmicpc.net/problem/5928

def main():
    # input
    d, h, m = map(int, input().split())
    
    minutes = (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)
    
    print(-1) if minutes < 0 else print(minutes)
    
if __name__ == '__main__':
    main()