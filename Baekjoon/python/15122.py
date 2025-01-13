# source : https://www.acmicpc.net/problem/15122

def main():
    # input
    num = input()
    
    while 1:
        num = str(int(num) + 1)
        
        if num.count('0') == 0:
            print(num)
            break

if __name__ == '__main__':
    main()