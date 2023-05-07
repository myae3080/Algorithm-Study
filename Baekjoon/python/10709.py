# source : https://www.acmicpc.net/problem/10709

def main():
    # input
    h, w = map(int, input().split())
    cloud = [[c for c in input()] for _ in range(h)]
    
    result = []
    for i in range(h):
        row = cloud[i]
        result_row = ['0'] * w
        result_row[0] = '0' if row[0] == 'c' else '-1'
        
        for j in range(1, w):
            if row[j] != 'c':
                if result_row[j - 1] == '-1':
                    result_row[j] = '-1'
                else:
                    result_row[j] = str(int(result_row[j - 1]) + 1)
        
        result.append(result_row)
    
    [print(' '.join(result[i])) for i in range(h)]

if __name__ == '__main__':
    main()