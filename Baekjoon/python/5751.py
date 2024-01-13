# source : https://www.acmicpc.net/problem/5751

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
    
        # input
        mary_wons = list(map(int, input().split())).count(0)
        
        print('Mary won %d times and John won %d times' % (mary_wons, n - mary_wons))

if __name__ == '__main__':
    main()