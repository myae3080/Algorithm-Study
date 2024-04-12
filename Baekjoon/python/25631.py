# source : https://www.acmicpc.net/problem/25631

def main():
    # input
    n = int(input())
    dolls = list(map(int, input().split()))
    
    temp = sorted(dolls, reverse=True)
    
    result = 0
    while temp:
        for doll in set(temp):
            del temp[temp.index(doll)]
        
        result += 1
    
    print(result)
    
if __name__ == '__main__':
    main()