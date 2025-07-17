# source : https://www.acmicpc.net/problem/33810

def main():
    # input
    S = input()
    
    favorite = 'SciComLove'
    result = 0
    for i in range(len(favorite)):
        if S[i] != favorite[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()