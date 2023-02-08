# source : https://www.acmicpc.net/problem/2948

import datetime

def main():
    # input
    d, m = map(int, input().split())
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    print(days[datetime.datetime(2009, m, d).weekday()])

if __name__ == '__main__':
    main()