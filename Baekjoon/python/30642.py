# source : https://www.acmicpc.net/problem/30642

def main():
    # input
    n = int(input())
    mascot = input()
    k = int(input())
    
    if mascot == 'annyong':
        if k % 2 == 1:
            print(k)
        else:
            print(k + 1 if k + 1 <= n else k - 1)
    else:
        if k % 2 == 0:
            print(k)
        else:
            print(k + 1 if k + 1 <= n else k - 1)

if __name__ == '__main__':
    main()