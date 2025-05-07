# source : https://www.acmicpc.net/problem/18679

def main():
    word_dict = {}
    
    # input
    for _ in range(int(input())):
        # input
        key, e, value = input().split()
        
        word_dict[key] = value
    
    # input
    for _ in range(int(input())):
        # input
        K = int(input())
        words = list(input().split())
        
        print(' '.join([word_dict[word] for word in words]))

if __name__ == '__main__':
    main()