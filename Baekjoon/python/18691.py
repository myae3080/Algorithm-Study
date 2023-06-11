# source : https://www.acmicpc.net/problem/18691

def main():
    # input
    for _ in range(int(input())):
        # input
        g, c, e = map(int, input().split())
        
        k = e - c
        
        if k < 0:
            print(0)
        else:
            if g == 1:
                print(k)
            elif g == 2:
                print(3 * k)
            else:
                print(5 * k)

if __name__ == '__main__':
    main()