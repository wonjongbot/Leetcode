class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)
        for word in strs:
            sortedword = sorted(word)
            anaDict[tuple(sortedword)].append(word)
        return anaDict.values()