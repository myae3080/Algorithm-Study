# source : https://www.acmicpc.net/problem/27522

def main():
    # input
    racers = [(input().split()) for _ in range(8)]
    
    pts = [10, 8, 6, 5, 4, 3, 2, 1]
    racers.sort()
    
    red, blue = 0, 0
    for idx, racer in enumerate(racers):
        if racer[1] == 'R':
            red += pts[idx]
        else:
            blue += pts[idx]
    
    print('Red') if red > blue else print('Blue')
    
if __name__ == '__main__':
    main()