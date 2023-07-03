# source : https://www.acmicpc.net/problem/23805

def main():
    # input
    n = int(input())
    
    for i in range(5 * n):
        if i // n == 0:
            print('@@@' * n + ' ' * n + '@' * n)
        elif i // n == 4:
            print('@' * n + ' ' * n + '@@@' * n)
        else:
            print('@' * n + ' ' * n + '@' * n + ' ' * n + '@' * n)

if __name__ == '__main__':
    main()