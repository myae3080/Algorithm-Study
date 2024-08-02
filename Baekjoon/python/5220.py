# source : https://www.acmicpc.net/problem/5220

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        print('Valid' if int(bin(a)[2:].count('1')) % 2 == b else 'Corrupt')
        
if __name__ == '__main__':
    main()