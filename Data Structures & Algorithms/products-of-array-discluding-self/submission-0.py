class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output = [1] *n
        prefix = 1
        for i in range (n):
            output[i] = prefix
            prefix *= nums[i]
        sufix = 1
        for i in range(n-1,-1,-1):
            output[i] *= sufix
            sufix *= nums[i]
        return output


        