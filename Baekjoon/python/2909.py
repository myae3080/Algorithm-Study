# source : https://www.acmicpc.net/problem/2909

def main():
    # input
    price, zero = map(int, input().split())
    
    if len(str(price)) == zero and str(price)[0] == '5':
        print(10 ** zero)
    else:
        print(round(price, -zero))
    

if __name__ == '__main__':
    main()