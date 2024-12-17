# source : https://www.acmicpc.net/problem/26350

def main():
    # input
    for _ in range(int(input())):
        # input
        coin_info = list(input().split())
        
        coin = coin_info[1:]
        is_good = True
        for i in range(1, len(coin)):
            if int(coin[i]) < int(coin[i - 1]) * 2:
                is_good = False
                break
        
        print('Denominations: %s' % ' '.join(coin))
        print('%s coin denominations!' % ('Good' if is_good else 'Bad'))
        print()

if __name__ == '__main__':
    main()