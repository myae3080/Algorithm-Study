# source : https://www.acmicpc.net/problem/20650

def main():
    # input
    integers = sorted(list(map(int, input().split())))
    
    print(integers[0], integers[1], integers[-1] - sum(integers[:2]))

if __name__ == '__main__':
    main()