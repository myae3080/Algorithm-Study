# source : https://www.acmicpc.net/problem/17889

def main():
    # input
    y = int(input())
    
    month = 2018 * 12 + 3
    
    has_optimal = False
    while (month // 12) <= y:
        if (month // 12) == y:
            has_optimal = True
            break
        
        month += 26
    
    print('yes' if has_optimal else 'no')

if __name__ == '__main__':
    main()