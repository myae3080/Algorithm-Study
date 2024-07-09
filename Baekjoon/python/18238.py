# source : https://www.acmicpc.net/problem/18238

def main():
    # input
    alphabet = input()
    
    result = 0
    prev = 'A'
    for a in alphabet:
        left = ord(a) - ord(prev)
        right = ord(prev) - ord(a)
        
        left = left + 26 if left < 0 else left
        right = right + 26 if right < 0 else right
        
        result += min(left, right)
        
        prev = a
    
    print(result)

if __name__ == '__main__':
    main()