# source : https://www.acmicpc.net/problem/11131

def main():
    for _ in range(int(input())):
        # input
        N = int(input())
        weights = list(map(int, input().split()))
        
        total = sum(weights)
        if total == 0:
            print('Equilibrium')
        else:
            print('Right' if total > 0 else 'Left')

if __name__ == '__main__':
    main()