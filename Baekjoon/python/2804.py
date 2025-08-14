# source : https://www.acmicpc.net/problem/2804

def main():
    # input
    A, B = input().split()

    row_idx, col_idx = 0, 0
    row_len, col_len = len(A), len(B)
    for i in range(row_len):
        is_crossed = False
        for j in range(col_len):
            if A[i] == B[j]:
                row_idx, col_idx = j, i
                is_crossed = True
                
                break
        
        if is_crossed:
            break
    
    colNum = 0
    for i in range(col_len):
        if i == row_idx:
            print(A)
        else:
            print('.' * col_idx + B[colNum] + '.' * (row_len - col_idx - 1))
        
        colNum += 1

if __name__ == '__main__':
    main()