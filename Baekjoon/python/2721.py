# source : https://www.acmicpc.net/problem/2721

def main():
    # input
    t = int(input())
    
    for _ in range(t):
        # input
        n = int(input())
        
        result = 0
        for k in range(1, n + 1):
            T = 0
            
            for i in range(1, k + 2):
                T += i
            
            result += (k * T)
            
        print(result)
    
if __name__ == '__main__':
    main()