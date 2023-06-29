# source : https://www.acmicpc.net/problem/15232

def main():
    # input
    r, c = int(input()), int(input())
    
    [print('*' * c) for _ in range(r)]
        
if __name__ == '__main__':
    main()