# source : https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = [word]
            else:
                anagrams_dict[sorted_word].append(word)
                
        return anagrams_dict.values()
            