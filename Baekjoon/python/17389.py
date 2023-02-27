# source : https://www.acmicpc.net/problem/17389

def main():
    # input
    n = int(input())
    answer = input()
    
    scores = 0
    bonus = 0
    for i in range(n):
        if answer[i] == 'O':
            scores += (i + 1) + bonus
            bonus += 1
        else:
            bonus = 0
    
    print(scores)
            
if __name__ == '__main__':
    main()