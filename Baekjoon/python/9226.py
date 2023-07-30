# source : https://www.acmicpc.net/problem/9226

def main():
    while 1:
        # input
        word = input()
        
        if word == '#':
            break
        
        i = 0
        has_ay = False
        while i < len(word):
            i += 1
            
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                has_ay = True
                print(''.join(word) + 'ay')
                break
            
            word = word[1:] + word[0]
            
        if not has_ay:
            print(''.join(word) + 'ay')
        
if __name__ == '__main__':
    main()