class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letterMap = {"".join(sorted(x)):[] for x in strs}

        for x in strs:
            if "".join(sorted(x)) in letterMap.keys():
                letterMap["".join(sorted(x))].append(x)
            
        res = []
        i=0
        for k,v in letterMap.items():
            res.append(v)

        return res