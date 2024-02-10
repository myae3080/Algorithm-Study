# source : https://www.acmicpc.net/problem/26265

import sys
input = sys.stdin.readline

def main():
    mentos = set()
    menti_by_mento = {}
    
    # input
    for _ in range(int(input())):
        # input
        mento, menti = input().split()
        
        mentos.add(mento)
        if mento in menti_by_mento:
            menti_by_mento[mento].append(menti)
        else:
            menti_by_mento[mento] = [menti]
    
    for mento in sorted(mentos):
        for menti in sorted(menti_by_mento[mento], reverse=True):
            print(mento, menti)

if __name__ == '__main__':
    main()