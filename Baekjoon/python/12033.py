# source : https://www.acmicpc.net/problem/12033

def main():
    # input
    for t in range(int(input())):
        # input
        n = int(input())
        prices = list(map(int, input().split()))
        
        result = []
        for price in prices:
            if len(result) >= n:
                break
            
            cost = price * 4 // 3
            if cost in prices:
                result.append(str(price))
                prices.remove(cost)
        
        print('Case #%d: %s' % ((t + 1), ' '.join(result)))

if __name__ == '__main__':
    main()