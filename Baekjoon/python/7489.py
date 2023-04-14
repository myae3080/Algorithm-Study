# source : https://www.acmicpc.net/problem/7489

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        num = 1
        for i in range(2, n + 1):
            num *= i
        
        strNum = str(num)
        for i in range(len(strNum) - 1, -1, -1):
            if strNum[i] != '0':
                print(strNum[i])
                break
            
if __name__ == '__main__':
    main()