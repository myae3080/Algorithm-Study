# source : https://www.acmicpc.net/problem/21736

def main():
    # input
    n, m = map(int, input().split())
    
    campus = []
    to_visit = []
    visited = [[False] * m for _ in range(n)]
    for x in range(n):
        # input
        row = list(input())
        
        campus.append(row)
        for y in range(m):
            if row[y] == 'I':
                to_visit.append((x, y))
                visited[x][y] = True
    
    result = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while (to_visit):
        x, y = to_visit.pop(0)
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < n and 0 <= new_y < m:
                if campus[new_x][new_y] != 'X' and not visited[new_x][new_y]:
                    if campus[new_x][new_y] == 'P':
                        result += 1
                    
                    to_visit.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    
    print(result if result else 'TT')

if __name__ == '__main__':
    main()