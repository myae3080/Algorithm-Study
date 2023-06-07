# source : https://www.acmicpc.net/submit/21312

def main():
    # input
    beverages = list(map(int, input().split()))
    
    odds = []
    for beverage in beverages:
        if beverage % 2 == 1:
            odds.append(beverage)
    
    result = 1
    if len(odds) == 0:
        for beverage in beverages:
            result *= beverage
    else:
        for odd in odds:
            result *= odd
    
    print(result)

if __name__ == '__main__':
    main()