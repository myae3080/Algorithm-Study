# source : https://www.acmicpc.net/problem/28455

def main():
    # input
    N = int(input())
    levels = sorted([int(input()) for _ in range(N)], reverse=True)
    
    stat = 0
    for l in levels[:42]:
        if l >= 250:
            stat += 5
        elif l >= 200:
            stat += 4
        elif l >= 140:
            stat += 3
        elif l >= 100:
            stat += 2
        elif l >= 60:
            stat += 1
    
    print(sum(levels[:42]), stat)

if __name__ == '__main__':
    main()