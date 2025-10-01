# source : https://www.acmicpc.net/problem/25773

def main():
    # input
    numbers = list(input())

    numbers.sort(reverse=True)

    print(''.join(numbers))

if __name__ == '__main__':
    main()