# source : https://www.acmicpc.net/problem/23795

def main():
    result = 0
    while 1:
        # input
        money = int(input())
        
        if money == -1:
            break
        
        result += money
    
    print(result)

if __name__ == '__main__':
    main()