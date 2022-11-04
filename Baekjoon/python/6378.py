# source : https://www.acmicpc.net/problem/6378

def getRoot(n):
    return (n // 10) + (n % 10)

while True:
    # input
    num = int(input())
    
    if num == 0:
        break
    
    root = getRoot(num)
    while root > 9:
        root = getRoot(root)
        
    print(root)