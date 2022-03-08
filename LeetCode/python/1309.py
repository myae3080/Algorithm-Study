# source : https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        length = len(s)
        i = 0
        result = []
        
        while i < length:
            if i + 2 < length and s[i + 2] == '#':
                result.append(s[i:i + 2])
                i += 3
            else:
                result.append(s[i])
                i += 1
        
        return ''.join([chr(96 + int(s)) for s in result])