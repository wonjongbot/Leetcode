class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydic = {}
        for c in nums:
            mydic[c] = 0
        for c in nums:
            mydic[c] += 1
        for c in mydic:
            if mydic[c] >= 2:
                return True
        return False