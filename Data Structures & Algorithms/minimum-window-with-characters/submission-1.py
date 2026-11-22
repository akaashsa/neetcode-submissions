class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #OUZAZADXYAAYZ #XYZ
        # ZADXY {Z:1+1, X:1, Y:1}
        # move j till all characters are covered atleast once, then one by one move i till all characters are covered with frequency with which they appear in t if freq requirement isnt meeting move j, untill all are covered and then repeat the same steps once all are found, at everytime the window is completed record the length

        # cover minimum required frequency
        # once achieved record the min window
        # shrink window till minimum reqd. is fulfiled and move i to j
        # return the window

        freq = {} # frequency covered so far
        reqd = Counter(t) # minimum reqd. for each

        length = float("inf")
        ans = ""
        n = len(s)
        i = 0
        j = 0
        matched = 0

        while j<n:
            if s[j] in t:
                if not freq:
                    i = j

                freq[s[j]] = freq.get(s[j],0)+1

                if freq[s[j]] == reqd[s[j]]:
                    matched +=1 
                while matched ==len(reqd):
                    length = min(length, j-i+1)
                    ans = s[i:j+1] if j-i+1 <= length else ans                    
                    if s[i] in freq:
                        freq[s[i]] -=1
                        if freq[s[i]] < reqd[s[i]]:
                            matched -=1
                    
                    i +=1
            
            j +=1

        
        return ans

