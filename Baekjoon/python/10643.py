# source : https://www.acmicpc.net/problem/10643

def main():
    # input
    mushrooms = [int(input()) for _ in range(8)]
    
    result = 0
    for i in range(4):
        result = max(result, sum(mushrooms[i:i + 4]), sum(mushrooms[i + 4:8] + mushrooms[:i]))
        
    print(result)
        
if __name__ == '__main__':
    main()