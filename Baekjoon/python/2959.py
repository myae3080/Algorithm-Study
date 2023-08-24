# source : https://www.acmicpc.net/problem/2959

def main():
    # input
    steps = sorted(map(int, input().split()))
    
    print(steps[0] * steps[-2])
    
if __name__ == '__main__':
    main()