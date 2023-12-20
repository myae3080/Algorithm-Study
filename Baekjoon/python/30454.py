# source : https://www.acmicpc.net/problem/30454

def main():
    # input
    n, l = map(int, input().split())
    
    zebra_furs = []
    for _ in range(n):
        # input
        zebra = input()
        
        black = 1 if zebra[0] == '1' else 0
        for i in range(1, l):
            if zebra[i - 1] != zebra[i] and zebra[i] == '1':
                black += 1
    
        zebra_furs.append(black)
        
    print(max(zebra_furs), zebra_furs.count(max(zebra_furs)))

if __name__ == '__main__':
    main()