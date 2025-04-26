# source : https://www.acmicpc.net/problem/26307

def main():
    # input
    hh, mm = map(int, input().split())

    print((hh - 9) *60 +mm)
    
if __name__ == '__main__':
    main()