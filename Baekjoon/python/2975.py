# source : https://www.acmicpc.net/problem/2975

def main():
    while 1:
        # input
        balance, action, money = input().split()
        
        if balance == money == '0' and action == 'W':
            break
        
        if action == 'W':
            b = int(balance) - int(money)
            if b < -200:
                print('Not allowed')
            else:
                print(b)
        else:
            print(int(balance) + int(money))

if __name__ == '__main__':
    main()