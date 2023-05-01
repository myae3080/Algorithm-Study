# source : https://www.acmicpc.net/problem/11292

def main():
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        # input
        students = [(input().split()) for _ in range(n)]
        
        students.sort(key = lambda s: s[1], reverse=True)
        max_height = students[0][1]
        
        [print(tu[0], end=' ') for tu in students if tu[1] == max_height]
        
if __name__ == '__main__':
    main()