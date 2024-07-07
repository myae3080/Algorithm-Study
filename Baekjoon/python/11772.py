# source : https://www.acmicpc.net/problem/11772

def main():
    # input
    N = int(input())
    
    result = 0
    for _ in range(N):
        # input
        text = input()
        
        result += int(text[:len(text) - 1]) ** int(text[-1])
    
    print(result)

if __name__ == '__main__':
    main()