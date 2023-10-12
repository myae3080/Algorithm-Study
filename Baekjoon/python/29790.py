# source : https://www.acmicpc.net/problem/29790

def main():
    # input
    N, U, L = map(int, input().split())
    
    if N < 1000:
        print('Bad')
    elif U >= 8000 or L >= 260:
        print('Very Good')
    else:
        print('Good')

if __name__ == '__main__':
    main()