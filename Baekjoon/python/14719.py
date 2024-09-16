# source : https://www.acmicpc.net/problem/14719

def main():
    # input
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))
    
    left_wall, right_wall = 0, 0
    water = 0
    for i in range(1, W - 1):
        left_wall = max(heights[:i])
        right_wall = max(heights[i + 1:])
        
        wall = min(left_wall, right_wall)
        if wall > heights[i]:
            water += wall - heights[i]
    
    print(water)

if __name__ == '__main__':
    main()