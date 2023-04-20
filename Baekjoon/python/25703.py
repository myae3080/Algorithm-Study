# source : https://www.acmicpc.net/problem/25703

def main():
    # input
    n = int(input())
    
    print('int a;')
    print('int *ptr = &a;')
    
    for i in range(2, n + 1):
        if i == 2:
            print('int {0}ptr{1} = &ptr;'.format('*' * i, i))
        else:
            print('int {0}ptr{1} = &ptr{2};'.format('*' * i, i, i - 1))
    
if __name__ == '__main__':
    main()