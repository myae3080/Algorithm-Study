# source : https://www.acmicpc.net/problem/1340

def main():
    # input
    monthDay, yearTime = input().split(',')
    
    month, day = monthDay.split()
    year, time = yearTime.split()
    hh, mm = time.split(':')
    
    days_by_month = {
        'January': 0,
        'February': 31,
        'March': 59,
        'April': 90,
        'May': 120,
        'June': 151,
        'July': 181,
        'August': 212,
        'September': 243,
        'October': 273,
        'November': 304,
        'December': 334,
    }
    
    total_mins = 365 * 24 * 60
    curr_mins = ((days_by_month[month] + int(day) - 1) * 24 * 60) + ((int(hh) * 60) + int(mm))
    
    if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0):
        total_mins += (24 * 60)
        
        if days_by_month[month] >= 59:
            curr_mins += (24 * 60)
            
    print((curr_mins / total_mins) * 100)
    
if __name__ == '__main__':
    main()