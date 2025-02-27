# source : https://www.acmicpc.net/problem/21631

def main():
    # input
    a, b = map(int, input().split())
    
    if b == 0:
        print(0)
        
        return
    
    if a >= b:
        print(b)
    else:
        print(a + 1)

if __name__ == '__main__':
    main()