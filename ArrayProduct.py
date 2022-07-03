    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2: 
            return [0]*len(nums)
        if nums.count(0) == 1:
            result = [0]*len(nums)
            i = nums.index(0)
            nums.remove(0)
            result[i] = prod(nums)
            return result
        totalProd = prod(nums)
        answer = [totalProd // num for num in nums]
        return answer
