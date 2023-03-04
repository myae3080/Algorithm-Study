# source : https://www.acmicpc.net/problem/22864

def main():
    # input
    a, b, c, m = map(int, input().split())
    
    work = 0
    fatigue = 0
    h = 0
    while h < 24:
        h += 1
        
        if fatigue + a > m:
            fatigue = max(0, fatigue - c)
            continue
        
        work += b
        fatigue += a
    
    print(work)

if __name__ == '__main__':
    main()