# source : https://www.acmicpc.net/problem/4659

vowels = ['a', 'e', 'i', 'o', 'u']

while 1:
    # input
    pw = input()
    
    if pw == 'end':
        break
    
    is_acceptable = False
    
    # condition 1
    for v in vowels:
        if pw.count(v) != 0:
            is_acceptable = True
            break
        
    if not is_acceptable:
        print('<{0}> is not acceptable.'.format(pw))
        continue
        
    # condition 2
    if len(pw) > 2:
        for i in range(len(pw) - 2):
            if (pw[i] not in vowels and pw[i + 1] not in vowels and pw[i + 2] not in vowels) or (pw[i] in vowels and pw[i + 1] in vowels and pw[i + 2] in vowels):
                is_acceptable = False
                break
            
    if not is_acceptable:
        print('<{0}> is not acceptable.'.format(pw))
        continue
    
    # condition 3
    if len(pw) > 1:
        for i in range(len(pw) - 1):
            if (pw[i] == pw[i + 1]) and (pw[i] != 'e' and pw[i] != 'o'):
                is_acceptable = False
                break
            
    if not is_acceptable:
        print('<{0}> is not acceptable.'.format(pw))
    else:
        print('<{0}> is acceptable.'.format(pw))