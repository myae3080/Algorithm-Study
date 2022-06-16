# source : https://www.acmicpc.net/problem/4447

'''
    time complextiy : O(n)
    space complexity : O(1)
'''
for _ in range(int(input())):
    # input
    string = input()

    good = string.lower().count('g')
    bad = string.lower().count('b')
    
    if good > bad:
        print(string, 'is GOOD')
    elif good < bad:
        print(string, 'is A BADDY')
    else:
        print(string, 'is NEUTRAL')