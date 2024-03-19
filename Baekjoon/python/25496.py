# source : https://www.acmicpc.net/problem/25496

def main():
    # input
    p, n = map(int, input().split())
    equpis = sorted(list(map(int, input().split())))
    
    fatigue = 200 - p
    
    if fatigue <= 0:
        print(0)
    else:
        result = 0
        for e in equpis:
            if fatigue > 0:
                fatigue -= e
                result += 1
            else:
                break
        
        print(result)

if __name__ == '__main__':
    main()