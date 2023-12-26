# source : https://www.acmicpc.net/problem/1773

def main():
    # input
    n, c = map(int, input().split())
    
    time = [0] * (c + 1)
    for _ in range(n):
        # input
        period = int(input())
        
        for t in range(period, c + 1, period):
            time[t] = 1
    
    print(sum(time))

if __name__ == '__main__':
    main()