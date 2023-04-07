# source : https://www.acmicpc.net/problem/25801

def main():
    # input
    inputStr = input()

    check = [0, 0]
    for c in set(inputStr):
        if inputStr.count(c) % 2:
            check[1] = 1
        else:
            check[0] = 1
    
    if check.count(1) == 2:
        print('0/1')
    elif check[0]:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()