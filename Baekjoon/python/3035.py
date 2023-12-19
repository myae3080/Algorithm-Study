# source : https://www.acmicpc.net/problem/3035

def main():
    # input
    r, c, zr, zc = map(int, input().split())
    scanned = [input() for _ in range(r)]
    
    for i in range(r * zr):
        result = ''
        for c in scanned[i // zr]:
            result += c * zc
        
        print(result)

if __name__ == '__main__':
    main()