class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","").lower()
        i,j=0,len(s)-1
        si=''
        sj=''
        while(i<j):
            if(s[i].isalnum() and s[j].isalnum()):
                if(s[i]==s[j]):
                    i+=1
                    j-=1
                    si+=s[i]
                    sj+=s[j]
                else:
                    print(si)
                    print(sj)
                    return False
            else:
                if(s[i].isalnum()):
                    j-=1
                else:
                    i+=1
        return True