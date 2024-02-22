# source : https://www.acmicpc.net/problem/15178

def main():
    # input
    for _ in range(int(input())):
        # input
        angles = input()
        
        angle_sum = sum([int(angle) for angle in angles.split(' ')])
        
        print('%s Seems OK' % angles if angle_sum == 180 else '%s Check' % angles)

if __name__ == '__main__':
    main()