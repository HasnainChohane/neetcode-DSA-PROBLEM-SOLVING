class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}
        result =[]
        for i ,num in enumerate(nums):
            val1 = target - num
            if val1 in val:
               result = [val[val1],i]
               break
            
            else:
                val[num]= i
                continue
        return result        
       
       
