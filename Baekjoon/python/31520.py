# source : https://www.acmicpc.net/problem/31520

def main():
    # input
    n = input()
    
    result = '0'
    while len(n) > 0:
        result = str(int(result) + 1)
        
        if n.startswith(result):
            n = n.replace(result, '', 1)
        else:
            result = -1
            break
    
    print(result)

if __name__ == '__main__':
    main()