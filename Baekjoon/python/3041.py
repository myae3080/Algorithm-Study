# source : https://www.acmicpc.net/problem/3041

def main():
    answer = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
    
    # input
    puzzle = [input() for _ in range(4)]
    
    diff_key = {}
    for i in range(4):
        for j in range(4):
            if answer[i][j] != puzzle[i][j] and puzzle[i][j] != '.':
                diff_key[puzzle[i][j]] = (i, j)
    
    result = 0
    for i in range(4):
        for j in range(4):
            if answer[i][j] in diff_key:
                result += abs(diff_key[answer[i][j]][0] - i) + abs(diff_key[answer[i][j]][1] - j)
    
    print(result)

if __name__ == '__main__':
    main()