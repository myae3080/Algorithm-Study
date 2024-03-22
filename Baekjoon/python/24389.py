# source : https://www.acmicpc.net/problem/24389

def main():
    # input
    n = int(input())
    
    n_bit = bin(n)[2:].zfill(32)
    complement = bin(int(''.join(['1' if b == '0' else '0' for b in n_bit]), 2) + 1)[2:].zfill(32)

    result = 0
    for i in range(len(n_bit)):
        if n_bit[i] != complement[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()