# source : https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        result = ''
        
        if length1 > length2:
            for i in range(length2):
                result += word1[i] + word2[i]
                
            result += word1[length2:]
        else:
            for i in range(length1):
                result += word1[i] + word2[i]
                
            result += word2[length1:]
            
        return result