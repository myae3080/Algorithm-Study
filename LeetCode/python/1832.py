# source : https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [0] * 26
        
        for c in sentence:
            alphabet[ord(c) - 97] = 1
                
        return False if alphabet.count(0) else True