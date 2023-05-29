# source : https://www.acmicpc.net/problem/26530

def main():
    # input
    for _ in range(int(input())):
        result = 0
        
        # input
        for __ in range(int(input())):
            # input
            name, quantity, price = input().split()
            
            result += float(quantity) * float(price)
        
        print('$' + '{:.2f}'.format(result))
        
if __name__ == '__main__':
    main()