# source : https://www.acmicpc.net/problem/12782

def main():
    # input
    for _ in range(int(input())):
        # input
        n, m = map(list, input().split())
        
        count_zero, count_one = 0, 0
        for i in range(len(n)):
            if n[i] != m[i]:
                if m[i] == '0':
                    count_zero += 1
                else:
                    count_one += 1
        
        print(max(count_zero, count_one))

if __name__ == '__main__':
    main()