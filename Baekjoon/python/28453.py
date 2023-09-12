# source : https://www.acmicpc.net/problem/28453

def main():
    # input
    n = int(input())
    levels = list(map(int, input().split()))

    result = []
    for level in levels:
        if level >= 300:
            result.append('1')
        elif level >= 275:
            result.append('2')
        elif level >= 250:
            result.append('3')
        else:
            result.append('4')
    
    print(' '.join(result))

if __name__ == '__main__':
    main()