# source : https://www.acmicpc.net/problem/13236

def main():
    # input
    n = int(input())
    
    result = [str(n)]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            result.append(str(n))
        else:
            n = n * 3 + 1
            result.append(str(n))

    print(' '.join(result))

if __name__ == '__main__':
    main()