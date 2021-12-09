# source : https://www.acmicpc.net/problem/1526
# math

# input
num = input()

while True:
    is_next = False
    
    for s in num:
        if s != "4" and s != "7":
            num = str(int(num) - 1)
            is_next = True
            break
        
    if not is_next:
        print(num)
        break