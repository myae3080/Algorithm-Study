# source : https://www.acmicpc.net/problem/1431

def onlyNumberDigitSum(string: str) -> int:
    result = 0
    
    for c in string:
        if c.isnumeric():
            result += int(c)
            
    return result

# input
serials = [input() for _ in range(int(input()))]

serials.sort(key = lambda string: (len(string), onlyNumberDigitSum(string), string))
[print(serial) for serial in serials]