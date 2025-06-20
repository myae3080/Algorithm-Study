# source : https://www.acmicpc.net/problem/13610

def main():
    # input
    X, Y = map(int, input().split())
    
    laps = 1
    while 1:
        if Y * laps - X * laps >= Y:
            print(laps)
            
            break
        
        laps += 1

if __name__ == '__main__':
    main()