# source : https://www.acmicpc.net/problem/13225

def main():
    # input
    n = int(input())
    
    for _ in range(n):
        # input
        num = int(input())
        
        result = 0
        for i in range(1, num + 1):
            if num % i == 0:
                result += 1
        
        print(num, result)

if __name__ == '__main__':
    main()