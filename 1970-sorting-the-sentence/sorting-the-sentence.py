class Solution:
    def sortSentence(self, s: str) -> str:
        ans=[]
        for i in s:
            if i.isdigit():
                ans.append(i)
        s=s.split()
        ans.sort()
        ans1=''
        for i in range(len(ans)):
            for j in s:
                if ans[i] in j:
                    j=j[:-1]
                    ans1+=j+' '
        return ans1[:-1]