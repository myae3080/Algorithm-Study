# source : https://www.acmicpc.net/problem/2765

from math import pi

def main():
    count = 0
    while 1:
        # input
        inch_diameter, rotation, sec = map(float, input().split())
        
        if rotation == 0:
            break
    
        count += 1
        mile_distance = inch_diameter / 12 / 5280 * pi * rotation
        mph = mile_distance / (sec / 3600)
        
        print('Trip #%d: %.2f %.2f' % (count, mile_distance, mph))
        
if __name__ == '__main__':
    main()