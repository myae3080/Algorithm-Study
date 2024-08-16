# source : https://www.acmicpc.net/problem/30214

def main():
    # input
    s1, s2 = map(int, input().split())
    
    print('E' if s1 >= s2 / 2 else 'H')

if __name__ == '__main__':
    main()