class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hashmap where key is a number and value is occurance of that number
        # then iterate through the numbers and try to find a longest consecutive numbers, save 
        # it into a variable named "ret"
        table = defaultdict(int)
        
        for c in nums:
            table[c] = 1;
        
        maxlength = 0
        
        for c in nums:
            if c-1 not in table:
                length = 0
                while (c+length) in table:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength
        
                
        