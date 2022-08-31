class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicA = {}
        dicB = {}
        for c in s:
            dicA[c] = 1
        for c in s:
            dicA[c] += 1
        
        for c in t:
            dicB[c] = 1
        for c in t:
            dicB[c] += 1
        
        if dicA == dicB:
            return True
        return False
        