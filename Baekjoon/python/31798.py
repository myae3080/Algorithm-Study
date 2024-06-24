# source : https://www.acmicpc.net/problem/31798

def main():
    # input
    a, b, c = map(int, input().split())
    
    if a == 0:
        print(int(c ** 2) - b)
    elif b == 0:
        print(int(c ** 2) - a)
    else:
        print(int((a + b) ** 0.5))

if __name__ == '__main__':
    main()