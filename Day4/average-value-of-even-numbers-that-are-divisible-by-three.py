class Solution(object):
    def averageValue(self, nums):
        sum=0
        count=0
        for n in nums:
            if n%6==0:
                sum+=n
                count+=1
        if count ==0:
            return 0
        else:
            return sum/count
        
