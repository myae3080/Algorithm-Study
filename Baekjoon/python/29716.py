# source : https://www.acmicpc.net/problem/29716

def main():
    # input
    j, n = map(int, input().split())
    
    result = 0
    for _ in range(n):
        # input
        sentence = input()
        
        total = 0
        for i in range(len(sentence)):
            if sentence[i].isupper():
                total += 4
            elif sentence[i].islower() or sentence[i].isdigit():
                total += 2
            elif sentence[i] == ' ':
                total += 1
                
        if j >= total:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()