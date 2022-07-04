class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #Brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans
        '''
        #Hashmap
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [i, seen[remaining]]
            
            seen[value] = i
            
            