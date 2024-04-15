# source : https://www.acmicpc.net/problem/31628

def main():
    # input
    eggplants = [input().split() for _ in range(10)]
    
    result = 0
    for i in range(10):
        if len(set(eggplants[i])) == 1:
            result = 1
            break
    
    if result == 0:
        for j in range(10):
            temp = set()
            for k in range(10):
                temp.add(eggplants[k][j])
            
            if len(temp) == 1:
                result = 1
                break
    
    print(result)

if __name__ == '__main__':
    main()