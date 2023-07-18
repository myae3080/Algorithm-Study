# source : https://www.acmicpc.net/problem/2704

def main():
    for _ in range(int(input())):
        # input
        h, m, s = map(int, input().split(':'))
        
        bin_h = list(bin(h)[2:].zfill(6))
        bin_m = list(bin(m)[2:].zfill(6))
        bin_s = list(bin(s)[2:].zfill(6))
        
        column_type = ''
        for i in range(6):
            column_type += bin_h[i] + bin_m[i] + bin_s[i]
        
        row_type = ''.join(bin_h + bin_m + bin_s)
        
        print(column_type, row_type)

if __name__ == '__main__':
    main()