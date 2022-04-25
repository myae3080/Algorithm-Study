# source : https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key = lambda string: string[-1])
        
        return ' '.join([string[:len(string) - 1] for string in words])