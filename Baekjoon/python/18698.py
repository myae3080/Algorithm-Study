# source : https://www.acmicpc.net/problem/18698

def main():
    # input
    T = int(input())
    
    for _ in range(T):
        # input
        walk = input()
        
        if 'D' in walk:
            print(len(walk[:walk.index('D')]))
        else:
            print(len(walk))

if __name__ == '__main__':
    main()