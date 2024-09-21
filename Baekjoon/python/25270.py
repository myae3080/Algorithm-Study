# source : https://www.acmicpc.net/problem/25270

def main():
    # input
    n = int(input())
    
    if n < 100:
        print(99)
    else:
        hundreds = n // 100
        
        bigger, smaller = hundreds * 100 + 99, (hundreds - 1) * 100 + 99
        if bigger - n <= n - smaller:
            print(bigger)
        else:
            print(smaller)

if __name__ == '__main__':
    main()