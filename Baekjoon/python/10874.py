# source : https://www.acmicpc.net/problem/10874

def main():
    # input
    n = int(input())
    
    answer = getAnswers()
    for i in range(1, n + 1):
        # input
        if answer == input():
            print(i)
        
def getAnswers():
    return ' '.join([str(((i - 1) % 5) + 1) for i in range(1, 11)])

if __name__ == '__main__':
    main()