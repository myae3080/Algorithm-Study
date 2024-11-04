# source : https://www.acmicpc.net/problem/32399

def main():
    # input
    S = input()
    
    if S == '(1)':
        print(0)
    elif S == ')1(':
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()