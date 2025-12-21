# source : https://www.acmicpc.net/problem/21354

def main():
    # input
    A, P = map(int, input().split())

    apple_price = A * 7
    pear_price = P * 13

    if apple_price > pear_price:
        print('Axel')
    elif apple_price < pear_price:
        print('Petra')
    else:
        print('lika')

if __name__ == '__main__':
    main()