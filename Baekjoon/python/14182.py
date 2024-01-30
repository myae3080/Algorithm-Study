# source : https://www.acmicpc.net/problem/14182

def main():
    while 1:
        # input
        income = int(input())
        
        if income == 0:
            break
        
        if income <= 1000000:
            print(income)
        elif income <= 5000000:
            print(int(income * 0.9))
        else:
            print(int(income * 0.8))

if __name__ == '__main__':
    main()