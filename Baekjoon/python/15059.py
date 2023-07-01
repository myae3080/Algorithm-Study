# source : https://www.acmicpc.net/problem/15059

def main():
    # input
    meals = list(map(int, input().split()))
    requests = list(map(int, input().split()))
    
    result = 0
    for i in range(3):
        if requests[i] > meals[i]:
            result += requests[i] - meals[i]
            
    print(result)

if __name__ == '__main__':
    main()