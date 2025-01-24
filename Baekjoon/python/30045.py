# source : https://www.acmicpc.net/problem/30045

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        S = input()
        
        if '01' in S or 'OI' in S:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()