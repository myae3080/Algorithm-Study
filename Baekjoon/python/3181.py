# source : https://www.acmicpc.net/problem/3181

def main():
    useless = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
    
    # input
    words = list(input().split())
    
    result = words[0][0].upper()
    for word in words[1:]:
        if useless.count(word) == 0:
            result += word[0].upper()
            
    print(result)
    
if __name__ == '__main__':
    main()