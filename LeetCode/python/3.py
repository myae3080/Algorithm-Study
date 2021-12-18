# source : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    # inefficient solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        max_num = 0
        
        for i in range(s_len):
            temp_list = []
            
            for j in range(i, s_len):
                temp = ord(s[j])
                
                if temp not in temp_list:
                    temp_list.append(temp)
                else:
                    max_num = max(max_num, len(temp_list))
                    break
                    
            max_num = max(max_num, len(temp_list))
                    
        return max_num