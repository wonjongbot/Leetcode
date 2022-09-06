class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1]*len(nums)
        prefix = [1]*len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i+1]
        
        #print(prefix)
        #print(postfix)
        
        ans = [1]*len(nums)
        for i in range(0, len(prefix)):
            ans[i] = prefix[i]*postfix[i]
        #print(ans)
        return ans