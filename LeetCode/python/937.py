# source : https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        copy, letters = logs[:], []
        
        for li in logs:
            if not li.split()[1].isdigit():
                letters.append(li)
                copy.remove(li)
                
        letters.sort(key=lambda li: (li.split()[1:], li.split()[0]))
    
        return letters + copy