# source : https://www.acmicpc.net/problem/12034

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        count = int(input())
        price = list(map(int, input().split()))
        
        discount = []
        while len(discount) < count:
            p = price.pop(0)
            origin_price = int(p // 0.75)
            
            if origin_price in price:
                discount.append(str(p))
                price.remove(origin_price)
        
        print('Case #%d: %s' % (i, ' '.join(discount)))

if __name__ == '__main__':
    main()