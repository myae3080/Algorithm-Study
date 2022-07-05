# source : https://www.acmicpc.net/problem/5555
# string, brute force

# input
string = input()

result = 0

for _ in range(int(input())):
    ring = input()
    length = len(ring)
    
    if ring.find(string) != -1:
        result += 1
    else:
        for i in range(length):
            ring = ring[1:length] + ring[:1]
            
            if ring.find(string) != -1:
                result += 1
                break

print(result)