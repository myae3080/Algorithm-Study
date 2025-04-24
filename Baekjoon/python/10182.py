# source : https://www.acmicpc.net/problem/10182

from math import log10

def main():
    # input
    for _ in range(int(input())):
        # input
        data = list(input().split())
        
        if data[0] == 'H':
            print("{:.2f}".format(-log10(float(data[2]))))
        else:
            print("{:.2f}".format(14 + log10(float(data[2]))))

if __name__ == '__main__':
    main()