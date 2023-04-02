# source : https://www.acmicpc.net/problem/11109

def main():
    # input
    t = int(input())
    for _ in range(t):
        # input
        d, n, s, p = map(int, input().split())
        
        serial = n * s
        parallel = d + (n * p)
        
        print('do not parallelize') if serial < parallel else print('does not matter') if serial == parallel else print('parallelize')
        
if __name__ == '__main__':
    main()