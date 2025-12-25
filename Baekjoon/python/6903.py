# source : https://www.acmicpc.net/problem/6903

def main():
    # input
    t, s, h = int(input()), int(input()), int(input())

    for _ in range(t):
        print('*' + ' ' * s + '*' + ' ' * s + '*')
    
    print('*' + '*' * s + '*' + '*' * s + '*')

    for _ in range(h):
        print(' ' * (s + 1) + '*')

if __name__ == '__main__':
    main()