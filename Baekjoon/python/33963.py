# source : https://www.acmicpc.net/problem/33963

def main():
    # input
    N = input()
    
    digits = len(N)
    result = 0
    while 1:
        N = str(int(N) * 2)
        
        if len(N) == digits:
            result += 1
        else:
            break
    
    print(result)

if __name__ == '__main__':
    main()