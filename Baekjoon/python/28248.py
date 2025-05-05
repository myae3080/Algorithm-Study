# source : https://www.acmicpc.net/problem/28248

def main():
    # input
    P, C = int(input()), int(input())

    score = P *50 + C * -10
    if P > C:
        score += 500
    
    print(score)

if __name__ == '__main__':
    main()