# source : https://www.acmicpc.net/problem/23813

def main():
    # input
    digits = list(input())
    
    print(sum([int(''.join(digits[i:] + digits[:i])) for i in range(len(digits))]))
        
if __name__ == '__main__':
    main()