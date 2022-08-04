# source : https://www.acmicpc.net/problem/1543

# input
document, word = input(), input()

length = len(word)
result = 0

while True:
    idx = document.find(word)
    if idx == -1:
        break
    else:
        result += 1
        document = document[idx + length:]
    
print(result)