# source : https://www.acmicpc.net/problem/7366

def main():
    # input
    for i in range(int(input())):
        # input
        m = int(input())
        words = list(input().split())
        
        print('Case %d: This list contains %d sheep.' % (i + 1, words.count('sheep')))
        print()

if __name__ == '__main__':
    main()