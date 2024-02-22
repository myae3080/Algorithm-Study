# source : https://www.acmicpc.net/problem/30031

def main():
    unit_by_width = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
    
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        w, h = map(int, input().split())
        
        result += unit_by_width[w]
    
    print(result)

if __name__ == '__main__':
    main()