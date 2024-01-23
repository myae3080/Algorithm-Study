# source : https://www.acmicpc.net/problem/28454

def main():
    # input
    curr_year, curr_month, curr_day = input().split('-')
    
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        year, month, day = input().split('-')
        
        if year > curr_year:
            result += 1
        elif year == curr_year:
            if month > curr_month:
                result += 1
            elif month == curr_month:
                if day >= curr_day:
                    result += 1
    
    print(result)

if __name__ == '__main__':
    main()