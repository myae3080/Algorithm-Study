# source : https://www.acmicpc.net/problem/3276

def main():
    # input
    N = int(input())
    
    a, b = 1, 1
    while a * b < N:
        if a > b:
            b += 1
        else:
            a += 1

    print(a, b)

if __name__ == '__main__':
    main()