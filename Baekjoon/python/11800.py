# source : https://www.acmicpc.net/problem/11800

def main():
    dice = {1: 'Yakk', 2: 'Doh', 3: 'Seh', 4: 'Ghar', 5: 'Bang', 6: 'Sheesh'}
    
    # input
    n = int(input())
    
    for i in range(1, n + 1):
        # input
        a, b = map(int, input().split())
        
        if a == b:
            if a == 1:
                print('Case {0}: {1}'.format(str(i), 'Habb Yakk'))
            elif a == 2:
                print('Case {0}: {1}'.format(str(i), 'Dobara'))
            elif a == 3:
                print('Case {0}: {1}'.format(str(i), 'Dousa'))
            elif a == 4:
                print('Case {0}: {1}'.format(str(i), 'Dorgy'))
            elif a == 5:
                print('Case {0}: {1}'.format(str(i), 'Dabash'))
            else:
                print('Case {0}: {1}'.format(str(i), 'Dosh'))
        else:
            if (a == 5 and b == 6) or (a == 6 and b == 5):
                print('Case {0}: {1}'.format(str(i), 'Sheesh Beesh'))
            else:
                print('Case {0}: {1} {2}'.format(str(i), dice.get(max(a, b)), dice.get(min(a, b))))

if __name__ == '__main__':
    main()