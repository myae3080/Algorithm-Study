# source : https://www.acmicpc.net/problem/4446

def main():
    vowels = ['a', 'i', 'y', 'e', 'o', 'u']
    consonants = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

    while 1:
        try:
            # input
            sentence = input()

            result = ''
            for c in sentence:
                is_upper = False
                if c.isupper():
                    is_upper = True
                    c = c.lower()
                
                if c in vowels:
                    changed_char = vowels[(vowels.index(c) + 3) % 6]
                    result += changed_char.upper() if is_upper else changed_char
                elif c in consonants:
                    changed_char = consonants[(consonants.index(c) + 10) % 20]
                    result += changed_char.upper() if is_upper else changed_char
                else:
                    result += c
            
            print(result)
        except:
            break

if __name__ == '__main__':
    main()