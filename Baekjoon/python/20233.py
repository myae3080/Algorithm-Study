# source : https://www.acmicpc.net/problem/20233

def main():
    # input
    a, x = int(input()), int(input())
    b, y = int(input()), int(input())
    t = int(input())
    
    print(a + max(t - 30, 0) * x * 21, b + max(t - 45, 0) * y * 21)
    
if __name__ == '__main__':
    main()