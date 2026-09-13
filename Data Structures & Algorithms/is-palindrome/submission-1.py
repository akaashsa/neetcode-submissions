class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s.lower())
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr.lower() == newStr[::-1].lower()