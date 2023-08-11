# source : https://www.acmicpc.net/problem/17945

def main():
    # input
    a, b = map(int, input().split())
    
    x1 = int(-a + ((a ** 2) - b) ** 0.5)
    x2 = int(-a - ((a ** 2) - b) ** 0.5)

    if x1 == x2:
        print(x1)
    else:
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
            
if __name__ == '__main__':
    main()