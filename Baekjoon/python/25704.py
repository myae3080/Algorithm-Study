# source : https://www.acmicpc.net/problem/25704

def main():
    # input
    stamp = int(input())
    price = int(input())
    
    discounts = []
    
    if stamp >= 5:
        discounts.append(500)
    
    if stamp >= 10:
        discounts.append(price // 10)
    
    if stamp >= 15:
        discounts.append(2000)
        
    if stamp >= 20:
        discounts.append(price // 4)
    
    if len(discounts) == 0:
        print(price)
    else:
        min_price = price - max(discounts)
        print(0) if min_price < 0 else print(min_price)
    
if __name__ == '__main__':
    main()