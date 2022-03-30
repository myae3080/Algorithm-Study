# source : https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        city = {}
        
        for path in paths:
            city[path[0]] = path[1]
        
        return list(city.values() - city.keys())[0]