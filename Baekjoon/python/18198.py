# source : https://www.acmicpc.net/problem/18198

def main():
    # input
    line = input()
    
    A, B = 0, 0
    for i in range(0, len(line), 2):
        if line[i] == 'A':
            A += int(line[i + 1])
        else:
            B += int(line[i + 1])
    
    print('A' if A > B else 'B')

if __name__ == '__main__':
    main()