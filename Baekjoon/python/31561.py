# source : https://www.acmicpc.net/problem/31561

def main():
    # input
    m = int(input())
    
    if m < 30:
        print(m / 2)
    else:
        print(((m - 30) * 3 / 2) + 15)

if __name__ == '__main__':
    main()