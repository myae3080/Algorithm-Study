# source : https://www.acmicpc.net/problem/26529

def main():
    fibo = [0] * 47
    fibo[1] = 1
    
    for i in range(2, 47):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
    # input
    for _ in range(int(input())):
        # input
        x = int(input())
        
        print(fibo[x + 1])

if __name__ == '__main__':
    main()