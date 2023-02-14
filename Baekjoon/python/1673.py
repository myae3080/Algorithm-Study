# source : https://www.acmicpc.net/problem/1673

def main():
    while 1:
        try:
            # input
            n, k = map(int, input().split())
        except EOFError:
            break
        
        result, stamp = n, n
        while stamp // k:
            result += stamp // k
            stamp = stamp // k + stamp % k
        
        print(result)
    
if __name__ == '__main__':
    main()