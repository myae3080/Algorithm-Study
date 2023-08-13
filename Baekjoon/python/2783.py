# source : https://www.acmicpc.net/problem/2783

def main():
    # input
    x, y = map(int, input().split())
    
    result = x / y * 1000 
    
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        result = min(result, a / b * 1000)
        
    print("{:.2f}".format(result))

if __name__ == '__main__':
    main()