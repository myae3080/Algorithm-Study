# source : https://www.acmicpc.net/problem/2858

def main():
    # input
    r, b = map(int, input().split())
    
    is_found = False
    for row in range(2000):
        if is_found:
            break
        
        for col in range(2000):
            if r == (col * 2) + (row - 2) * 2 and b == (col - 2) * (row - 2):
                print(max(row, col), min(row, col))
                is_found = True
                break

if __name__ == '__main__':
    main()