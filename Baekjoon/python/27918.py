# source : https://www.acmicpc.net/problem/27918

def main():
    # input
    n = int(input())
    winners = [input() for _ in range(n)]
    
    d, p = 0, 0
    for winner in winners:
        if winner == 'D':
            d += 1
        else:
            p += 1
        
        if abs(d - p) >= 2:
            break
    
    print(str(d) + ':' + str(p))

if __name__ == '__main__':
    main()