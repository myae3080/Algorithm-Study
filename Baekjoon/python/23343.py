# source : https://www.acmicpc.net/problem/23343

def main():
    # input
    x, y = input().split()
    
    if not x.isnumeric() or not y.isnumeric():
        print('NaN')
    else:
        print(int(x) - int(y))

if __name__ == '__main__':
    main()