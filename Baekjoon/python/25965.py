# source : https://www.acmicpc.net/problem/25965

def main():
    # input
    for _ in range(int(input())):
        # input
        missions = [list(map(int, input().split())) for _ in range(int(input()))]
        k, d, a = map(int, input().split())
    
        result = 0
        for mission in missions:
            price = mission[0] * k - mission[1] * d + mission[2] * a
            
            if price >= 0:
                result += price
        
        print(result)

if __name__ == '__main__':
    main()