# source : https://www.acmicpc.net/problem/30868

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        five = n // 5
        one = n % 5
        
        for _ in range(five):
            print('++++', end=' ')
        
        for _ in range(one):
            print('|', end='')
        
        print()

if __name__ == '__main__':
    main()