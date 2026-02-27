class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math as m
        root= int(m.sqrt(n))
        flag=True
        if root**2==n and root!=1:
            for x in range(2,root):
                if n%x==0:
                    flag =  False
        else:
            flag =  False
        return flag 
