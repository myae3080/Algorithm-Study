# source : https://www.acmicpc.net/problem/28432

def main():
    # input
    n = int(input())
    words = [input() for _ in range(n)]
    m = int(input())
    candidates = [input() for _ in range(m)]
    
    if len(words) == 1:
        print(candidates[0])
    else:
        q_idx = words.index('?')
        if q_idx == 0:
            first, last = '', words[q_idx + 1][0] 
        elif q_idx == len(words) - 1:
            first, last = words[q_idx - 1][-1], ''
        else:
            first, last = words[words.index('?') - 1][-1], words[words.index('?') + 1][0]
        
        for word in candidates:
            if word not in words:
                if q_idx == 0:
                    if word[-1] == last:
                        print(word)
                        break
                elif q_idx == len(words) - 1:
                    if word[0] == first:
                        print(word)
                        break
                else:
                    if word[0] == first and word[-1] == last:
                        print(word)
                        break

if __name__ == '__main__':
    main()