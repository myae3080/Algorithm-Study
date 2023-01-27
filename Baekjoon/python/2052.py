# source : https://www.acmicpc.net/problem/2052

def main():
    # input
    n = int(input())


    decimal = '{:.250f}'.format(1 / (2 ** n)) 
    target_idx = len(decimal)
    
    for i in range(len(decimal) - 1, 1, -1):
        if decimal[i] != '0':
            target_idx = i + 1
            break
    
    print(decimal[:target_idx])

if __name__ == '__main__':
    main()