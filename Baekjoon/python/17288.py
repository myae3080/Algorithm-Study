# source : https://www.acmicpc.net/problem/17288

# TODO

def main():
    # input
    S = input()

    cnt = 0
    for i in range(len(S) - 2):
        is_only_three = True
        if int(S[i]) + 2 == int(S[i + 1]) + 1 == int(S[i + 2]):
            if i - 1 >= 0:
                if int(S[i - 1]) + 1 == int(S[i]):
                    is_only_three = False
            if i + 3 < len(S):
                if int(S[i + 2]) + 1 == int(S[i + 3]):
                    is_only_three = False
        else:
            is_only_three = False
        
        if is_only_three:
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()