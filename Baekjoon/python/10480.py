# source : https://www.acmicpc.net/problem/10480

def main():
    # input
    for _ in range(int(input())):
        # input
        num = int(input())
        
        print('%d is even' % num if abs(num) % 2 == 0 else '%d is odd' % num)

if __name__ == '__main__':
    main()