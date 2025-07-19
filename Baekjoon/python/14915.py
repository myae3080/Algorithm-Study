# source : https://www.acmicpc.net/problem/14915

def main():
    # input
    m, n = map(int, input().split())
    
    if n == 2:
        print(bin(m)[2:])
    else:
        rest = []
        while m // n:
            rest.append(m % n)
            m //= n
            
        rest.append(m)
        
        print(''.join([chr(num + 55) if num >= 10 else str(num) for num in rest[::-1]]))

if __name__ == '__main__':
    main()