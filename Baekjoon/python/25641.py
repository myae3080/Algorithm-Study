# source : https://www.acmicpc.net/problem/25641

def main():
    # input
    n = int(input())
    st = list(input())
    
    while 1:
        if st.count('s') == st.count('t'):
            break
        else:
            st.pop(0)
    
    print(''.join(st))

if __name__ == '__main__':
    main()