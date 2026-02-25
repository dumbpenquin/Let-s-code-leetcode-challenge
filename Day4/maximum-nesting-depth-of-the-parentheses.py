class Solution(object):
    def maxDepth(self, s):
        count = 0
        lists=[]
        for x in s:
            if x=='(':
                count+=1
            elif x==')':
                lists.append(count)
                count-=1

        return max(lists or [0])
