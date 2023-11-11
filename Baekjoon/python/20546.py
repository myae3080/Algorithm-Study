# source : https://www.acmicpc.net/problem/20546

def main():
    # input
    cash_j = cash_s = int(input())
    prices = list(map(int, input().split()))
    
    bnp, timing = 0, 0
    # 준현
    for price in prices:
        if cash_j >= price:
            bnp += cash_j // price
            cash_j %= price

    # 성민
    for i in range(len(prices) - 4):
        if prices[i] < prices[i + 1] < prices[i + 2] < prices[i + 3]:
            cash_s += timing * prices[i + 3]
            timing = 0
        
        if prices[i] > prices[i + 1] > prices[i + 2] > prices[i + 3]:
            timing += cash_s // prices[i + 3]
            cash_s %= prices[i + 3]
    
    total_j = cash_j + bnp * prices[-1]
    total_s = cash_s + timing * prices[-1]

    if total_j > total_s:
        print('BNP')
    elif total_j < total_s:
        print('TIMING')
    else:
        print('SAMESAME')

if __name__ == '__main__':
    main()