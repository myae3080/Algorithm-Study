# source : https://www.acmicpc.net/problem/2846

def main():
    # input
    n = int(input())
    road = list(map(int, input().split()))
    
    uphils = []
    height = 0
    for i in range(1, n):
        if road[i - 1] < road[i]:
            height += road[i] - road[i - 1]
        else:
            height = 0
        
        uphils.append(height)
            
    print(max(uphils))

if __name__ == '__main__':
    main()