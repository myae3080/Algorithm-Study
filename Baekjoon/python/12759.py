# source : https://www.acmicpc.net/problem/12759

def main():
    board = [[0, 0, 0] for _ in range(3)]

    # input
    start_player = int(input())

    curr_player = start_player
    result = 0
    for _ in range(9):
        # input
        x, y = map(int, input().split())

        r, c = x - 1, y - 1
        board[r][c] = curr_player
        
        if result == 0:
            # row check
            if board[r].count(curr_player) == 3:
                result = curr_player

                continue
            
            # col check
            if [board[i][c] for i in range(3)].count(curr_player) == 3:
                result = curr_player

                continue
            
            # diagnol check
            if [board[i][i] for i in range(3)].count(curr_player) == 3:
                result = curr_player

                continue

            if [board[2 - i][i] for i in range(3)].count(curr_player) == 3:
                result = curr_player

                continue

        curr_player = 2 if curr_player == 1 else 1
        
    print(result)

if __name__ == '__main__':
    main()