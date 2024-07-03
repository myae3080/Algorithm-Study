# source : https://www.acmicpc.net/problem/12813

def main():
    # input
    a, b = int(input(), 2), int(input(), 2)

    digits = 100000

    print(bin(a & b)[2:].zfill(digits))
    print(bin(a | b)[2:].zfill(digits))
    print(bin(a ^ b)[2:].zfill(digits))
    print(''.join([str(1 - int(d)) for d in bin(a)[2:].zfill(digits)]))
    print(''.join([str(1 - int(d)) for d in bin(b)[2:].zfill(digits)]))
    
if __name__ == '__main__':
    main()