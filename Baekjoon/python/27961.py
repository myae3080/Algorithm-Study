# source : https://www.acmicpc.net/problem/27961

def main():
    # input
    N = int(input())
    
    if N == 0:
        print(0)
        return
    
    result, cats = 1, 1
    while cats < N:
        cats += cats
        result += 1
    
    print(result)

if __name__ == '__main__':
    main()