# source : https://www.acmicpc.net/problem/24510

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        word = input()
        
        result = max(result, word.count('for') + word.count('while'))
        
    print(result)

if __name__ == '__main__':
    main()