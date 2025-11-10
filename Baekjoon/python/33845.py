# source : https://www.acmicpc.net/problem/33845

def main():
    # input
    S, T = input(), input()

    t_list = list(T)
    for c in S:
        if c in t_list:
            t_list = [char for char in t_list if char != c]
    
    print(''.join(t_list))

if __name__ == '__main__':
    main()