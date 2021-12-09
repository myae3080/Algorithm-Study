# source : https://www.acmicpc.net/problem/1969
# string, bruteforcing

dnas = []
result, distance = '', 0

# input
n, m = map(int, input().split())
[dnas.append(list(input())) for _ in range(n)]

for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    
    for j in range(n):
        base = dnas[j][i]
    
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        else:
            t += 1
    
    major = max(a, c, g, t)
    distance += a + c + g + t - major 
    
    if major == a:
        result += "A"
    elif major == c:
        result += "C"
    elif major == g:
        result += "G"
    else:
        result += "T"
        
print(result)
print(distance)