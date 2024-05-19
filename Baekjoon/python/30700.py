# source : https://www.acmicpc.net/problem/30700

def main():
    # input
    s = input()
    
    korea = ['K', 'O', 'R', 'E', 'A']
    
    result, pointer = 0, 0
    for c in s:
        if c == korea[pointer % 5]:
            result += 1
            pointer += 1
    
    print(result)

if __name__ == '__main__':
    main()