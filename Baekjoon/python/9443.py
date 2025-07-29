# source : https://www.acmicpc.net/problem/9443

def main():
    chars = set()
    
    # input
    for _ in range(int(input())):
        # input
        s = input()
        
        chars.add(s[0])
    
    result = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for a in alpha:
        if a not in chars:
            break
        
        result += 1
    
    print(result)

if __name__ == '__main__':
    main()