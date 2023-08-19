# source : https://www.acmicpc.net/problem/2712

def main():
    # input
    for _ in range(int(input())):
        # input
        num, unit = input().split()
        
        if unit == 'kg':
            print('{:.4f} lb'.format(float(num) * 2.2046))
        elif unit == 'lb':
            print('{:.4f} kg'.format(float(num) * 0.4536))
        elif unit == 'l':
            print('{:.4f} g'.format(float(num) * 0.2642))
        else:
            print('{:.4f} l'.format(float(num) * 3.7854))

if __name__ == '__main__':
    main()