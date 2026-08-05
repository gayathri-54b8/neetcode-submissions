class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs,ct={},{}
        for i in s:
            cs[i]=(cs.get(i,) or 0)+1
        for i in t:
            ct[i]=(ct.get(i,) or 0)+1
        for i in cs:
            if cs[i]!=ct.get(i):
                return False
        return True