    """
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
    
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2: 
            return [0]*len(nums)
        if nums.count(0) == 1:
            result = [0]*len(nums)
            i = nums.index(0)
            nums.remove(0)
            result[i] = prod(nums)
            return result
        accumProduct = prod(nums)
        answer = [accumProduct // num for num in nums]
        return answer
