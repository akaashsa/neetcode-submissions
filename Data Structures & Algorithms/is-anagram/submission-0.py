class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s and t:
            s= sorted(s)
            t= sorted(t)
            print(s,' ',t)
        return s==t

            
        