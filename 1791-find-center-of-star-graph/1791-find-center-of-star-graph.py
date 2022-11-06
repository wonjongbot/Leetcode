class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        M = {}
        for e in edges:
            if e[0] in M:
                M[e[0]].append(e[1])
            else:
                M[e[0]] = [e[1]]
            if e[1] in M:
                M[e[1]].append(e[0])
            else:
                M[e[1]] = [e[0]]
        print(len(M))
        print(M)
        for val in M:
            if len(M[val])+1 == len(M):
                return val