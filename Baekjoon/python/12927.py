# source : https://www.acmicpc.net/problem/12927

def main():
    # input
    bulbs = ['N'] + list(input())
    
    if isCountYZero(bulbs):
        print(0)
        
        return 
    
    result = 0
    for i in range(1, len(bulbs)):
        if bulbs[i] == 'Y':
            for j in range(i, len(bulbs), i):
                if bulbs[j] == 'Y':
                    bulbs[j] = 'N'
                else:
                    bulbs[j] = 'Y'
        
            result += 1
        
        if isCountYZero(bulbs):
            print(result)
            
            return
    
    print(result if isCountYZero(bulbs) else -1)
    
def isCountYZero(bulbs: list) -> bool:
    return bulbs.count('Y') == 0

if __name__ == '__main__':
    main()