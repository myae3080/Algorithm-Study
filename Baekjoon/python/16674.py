# source : https://www.acmicpc.net/problem/16674

def main():
    integers = [0] * 10
    
    # input
    num = input()
    
    for n in num:
        # 관련 없는 수
        if int(n) in [3, 4, 5, 6, 7, 9]:
            print(0)
            return
        
        integers[int(n)] += 1
    
    # 관련 있지만 밀접한 수 아님
    if integers[0] == 0 or integers[1] == 0 or integers[2] == 0 or integers[8] == 0:
        print(1)
    # 묶여있는 수
    elif integers[0] == integers[1] == integers[2] == integers[8]:
        print(8)
    # 밀접하지만 묶여있는 수 아님
    else:
        print(2)

if __name__ == '__main__':
    main()