# source : https://www.acmicpc.net/problem/30889

def main():
    seats = [['.'] * 20 for _ in range(10)]
    
    # input
    n = int(input())
    
    for _ in range(n):
        # input
        seat = input()
        
        row_idx = ord(seat[0]) - 65
        col_idx = int(seat[1:]) - 1
        
        seats[row_idx][col_idx] = 'o'

    for i in range(len(seats)):
        print(''.join(seats[i]))

if __name__ == '__main__':
    main()