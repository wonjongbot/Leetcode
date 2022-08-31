class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydic = {}
        for c in nums:
            if c in mydic:
                return True
            mydic[c] = 1
        return False