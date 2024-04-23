# source : https://www.acmicpc.net/problem/29722

def main():
    # input
    year, month, day = map(int, input().split('-'))
    period = int(input())
    
    day += period
    
    while day > 30:
        day -= 30
        month += 1
        
    while month > 12:
        month -= 12
        year += 1
    
    print('{0}-{1}-{2}'.format(str(year), str(month).zfill(2), str(day).zfill(2)))

if __name__ == '__main__':
    main()