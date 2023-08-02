# source : https://www.acmicpc.net/problem/4435

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        g_troops = list(map(int, input().split()))
        s_troops = list(map(int, input().split()))
        
        g_pts = [1, 2, 3, 3, 4, 10]
        s_pts = [1, 2, 2, 2, 3, 5, 10]
        
        g_power = sum(list(map(lambda x, y: x * y, g_troops, g_pts)))
        s_power = sum(list(map(lambda x, y: x * y, s_troops, s_pts)))
        
        if g_power > s_power:
            print('Battle {0}: Good triumphs over Evil'.format(i))
        elif g_power < s_power:
            print('Battle {0}: Evil eradicates all trace of Good'.format(i))
        else:
            print('Battle {0}: No victor on this battle field'.format(i))

if __name__ == '__main__':
    main()