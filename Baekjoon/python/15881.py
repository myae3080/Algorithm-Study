# source : https://www.acmicpc.net/problem/15881

def main():
    # input
    n = int(input())
    things = input()

    start = 0
    result = 0
    while 1:
        if 'pPAp' in things[start:]:
            start += things[start:].index('pPAp') + 4
            result += 1
        else:
            break
    
    print(result)

if __name__ == '__main__':
    main()