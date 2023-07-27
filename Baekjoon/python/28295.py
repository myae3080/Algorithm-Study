# source : https://www.acmicpc.net/problem/28295

def main():
    cardinal_pts = ['N', 'E', 'S', 'W']
    
    direction = 0
    for _ in range(10):
        # input
        t = int(input())
        
        direction += t
        direction %= 4
        
    print(cardinal_pts[direction])
        
if __name__ == '__main__':
    main()