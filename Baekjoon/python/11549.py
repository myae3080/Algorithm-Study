# source : https://www.acmicpc.net/problem/11549

def main():
    # input
    t = int(input())
    answers = list(map(int, input().split()))
    
    print(answers.count(t))
    
if __name__ == '__main__':
    main()