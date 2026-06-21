class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}
        
        for i ,num in enumerate(nums):
            val1 = target - num
            if val1 in val:
               return [val[val1],i]
           
            val[num]= i
                
         
       
       
