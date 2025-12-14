# source : https://www.acmicpc.net/problem/11874

def main():
    # input
    L, D, X = int(input()), int(input()), int(input())

    for i in range(L, D + 1):
        if sum([int(n) for n in str(i)]) == X:
            print(i)

            break
    
    for i in range(D, L - 1, -1):
        if sum([int(n) for n in str(i)]) == X:
            print(i)

            break

if __name__ == '__main__':
    main()