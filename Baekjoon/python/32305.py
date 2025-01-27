# source : https://www.acmicpc.net/problem/32305

def main():
    # input
    a, b = map(int, input().split())
    cost = int(input())
    
    charged_dozen = 0
    if (a * b) % 12 == 0:
        charged_dozen = (a * b) // 12
    else:
        charged_dozen = ((a * b) // 12) + 1
    
    print(charged_dozen * cost)

if __name__ == '__main__':
    main()