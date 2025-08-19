# source : https://www.acmicpc.net/problem/14954

def main():
    # input
    n = int(input())

    while 1:
        n = sum([int(c) ** 2 for c in str(n)])

        if n == 1:
            print('HAPPY')

            break
        
        if n == 4:
            print('UNHAPPY')

            break
    
if __name__ == '__main__':
    main()