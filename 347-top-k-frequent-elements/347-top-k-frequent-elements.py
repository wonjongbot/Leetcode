class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ansdict = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            ansdict[i] = 1 + ansdict.get(i,0)
        
        for i, j in ansdict.items():
            freq[j].append(i)
        
        ret = []
        
        for i in range(len(freq) -1, 0, -1):
            for c in freq[i]:
                ret.append(c)
            if len(ret) == k:
                return ret