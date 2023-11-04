# source : https://www.acmicpc.net/problem/1668

def main():
    # input
    n = int(input())
    trophies = [int(input()) for _ in range(n)]
    
    left = 1
    left_prev = trophies[0]
    for i in range(1, n):
        if trophies[i] > left_prev:
            left += 1
            left_prev = trophies[i]
            
    right = 1
    right_prev = trophies[-1]
    for i in range(n - 2, -1, -1):
        if trophies[i] > right_prev:
            right += 1
            right_prev = trophies[i]
    
    print(left)
    print(right)
        
if __name__ == '__main__':
    main()