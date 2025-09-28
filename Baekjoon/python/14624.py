# source : https://www.acmicpc.net/problem/14624

def main():
    # input
    N = int(input())

    if N % 2 == 0:
        print('I LOVE CBNU')
    else:
        for i in range(N // 2 + 2):
            if i == 0:
                print('*' * N)
            elif i == 1:
                symbol = [' '] * N
                last_index = N // 2
                symbol[last_index] = '*'

                print(''.join(symbol[:last_index + 1]))
            else:
                symbol = [' '] * N
                last_index = N // 2 + i - 1
                symbol[N // 2 - i + 1] = '*'
                symbol[last_index] = '*'

                print(''.join(symbol[:last_index + 1]))

if __name__ == '__main__':
    main()