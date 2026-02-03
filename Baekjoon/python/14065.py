# source : https://www.acmicpc.net/problem/14065

def main():
    # input
    x = float(input())

    result = 100.0 / ((1.609344 / 3.785411784) * x)
    print(f'{result:.6f}')

if __name__ == '__main__':
    main()