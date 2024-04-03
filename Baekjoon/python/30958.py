# source : https://www.acmicpc.net/problem/30958

def main():
    # input
    n = int(input())
    song = input()
    
    alphabet = [0 for _ in range(26)]
    exception = [' ', ',', '.']
    
    for c in song:
        if c in exception:
            continue
        else:
            alphabet[ord(c) - 97] += 1
    
    print(max(alphabet))

if __name__ == '__main__':
    main()