class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += str(len(s))+"#"+s
            
        return string

        
    def decode(self, s: str) -> List[str]:

        decode = []
        i = 0
        length = ""
        while i<len(s):
            
            
            if s[i] == '#':
                    decode.append(s[i+1:i+1+int(length)])
                    i += int(length)+1
                    length = ""
            else : 
                    length += s[i]
                    i += 1
            
        

        return decode