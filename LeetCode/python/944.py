# source : https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deletion_size = 0
        
        for i in range(len(strs[0])):
            columns = []
            
            for s in strs:
                columns.append(s[i])
                
            if columns != sorted(columns):
                deletion_size += 1
            
        return deletion_size