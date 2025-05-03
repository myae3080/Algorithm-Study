# source : https://www.acmicpc.net/problem/10188

def main():
    # input
    for _  in range(int(input())):
        # input
        col, row = map(int, input().split())

        for __ in range(row):
            print('X' * col)
        
        print()

if __name__ == '__main__':
    main()