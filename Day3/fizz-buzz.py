class Solution(object):
    def fizzBuzz(self, n):
        item=[]
        for i in range(n):
            if (i+1)%3==0 and (i+1)%5!=0:
                item.append("Fizz")  
            elif (i+1)%3!=0 and (i+1)%5==0:
                item.append("Buzz") 
            elif (i+1)%3==0 and (i+1)%5==0:
                item.append("FizzBuzz")    
            else:
                item.append(str(i+1))
        return item
