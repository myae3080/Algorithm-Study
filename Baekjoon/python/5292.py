# source : https://www.acmicpc.net/problem/5292

def main():
    # input
    number = int(input())
    
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('DeadMan', end='\n')
        elif i % 3 == 0:
            print('Dead', end='\n')
        elif i % 5 == 0:
            print('Man', end='\n')
        else:
            print(i, end=' ')

if __name__ == '__main__':
    main()