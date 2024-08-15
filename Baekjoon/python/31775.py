# source : https://www.acmicpc.net/problem/31775

def main():
    # input
    first_chars = sorted([input()[0] for _ in range(3)])
    
    print('GLOBAL' if first_chars == ['k', 'l', 'p'] else 'PONIX')

if __name__ == '__main__':
    main()