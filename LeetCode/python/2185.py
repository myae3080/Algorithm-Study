# source : https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:                
        return [word[:len(pref)] for word in words].count(pref)