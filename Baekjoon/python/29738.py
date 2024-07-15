# source : https://www.acmicpc.net/problem/29738

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        n = int(input())
        
        round = 'Round 1'
        
        if n <= 25:
            round = 'World Finals'
        elif n <= 1000:
            round = 'Round 3'
        elif n <= 4500:
            round = 'Round 2'
        
        print('Case #%d: %s' % (i, round))

if __name__ == '__main__':
    main()