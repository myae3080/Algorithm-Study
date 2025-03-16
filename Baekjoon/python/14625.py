# source : https://www.acmicpc.net/problem/14625

def main():
    # input
    sh, sm = map(int, input().split())
    eh, em = map(int, input().split())
    N = input()
    
    result = 0
    while 1:
        if N in str(sh).zfill(2) or N in str(sm).zfill(2):
            result += 1
        
        if sh == eh and sm == em:
            print(result)
            
            break
        
        sm += 1
        if sm == 60:
            sh += 1
            sm = 0

if __name__ == '__main__':
    main()