# source : https://www.acmicpc.net/problem/16316

def main():
    # input
    n = int(input())
    count = list(input().split())
    
    num = 1
    for i in range(n):
        if count[i] != 'mumble' and count[i] != str(num):
            print('something is fishy')
            return
        
        num += 1
    
    print('makes sense')

if __name__ == '__main__':
    main()