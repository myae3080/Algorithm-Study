# source : https://www.acmicpc.net/problem/31009

def main():
    # input
    n = int(input())
    
    prices = []
    for _ in range(n):
        # input
        city, price = input().split()
        
        if city == 'jinju':
            j_price = int(price)
        
        prices.append(int(price))
    
    result = len([price for price in prices if price > j_price])
    
    print(j_price)
    print(result)
    
if __name__ == '__main__':
    main()