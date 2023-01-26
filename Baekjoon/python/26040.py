# source : https://www.acmicpc.net/problem/26040

def main():
    # input
    result = input()
    targets = input().split()
    
    for c in targets:
        result = result.replace(c, c.lower())
        
    print(result)
    
if __name__ == '__main__':
    main()