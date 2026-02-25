class Solution(object):
    def returnToBoundaryCount(self, nums):
        
        boun = 0 
        count=0
        for n in nums:
            boun =boun +n
            if boun ==0:
                count+=1
        return count
