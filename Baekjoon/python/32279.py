# source : https://www.acmicpc.net/problem/32279

def main():
    # input
    n = int(input())
    p, q, r, s = map(int, input().split())
    a = int(input())
    
    i = 1
    serial = [0, a]
    while 1:
        if 2 * i <= n:
            serial.append(p * serial[i] + q)
        if 2 * i + 1 <= n:
            serial.append(r * serial[i] + s)
            i += 1
        else:
            break
    
    print(sum(serial))

if __name__ == '__main__':
    main()