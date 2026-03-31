class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                for j in t:
                    if i == j:
                        t=t.replace(i,'',1)
                        break
            if len(t)!=0:
                return False
            return True