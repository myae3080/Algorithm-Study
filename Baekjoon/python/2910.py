# source : https://www.acmicpc.net/problem/2910

# input
N, C = map(int, input().split())
message = input().split()

frequency = {}
for m in list(dict.fromkeys(message)):
    frequency[m] = message.count(m)

frequency = sorted(frequency.items(), key=lambda tu:tu[1], reverse=True)

result = ''
for tu in frequency:
    result += ((tu[0] + ' ') * tu[1])
    
print(result)