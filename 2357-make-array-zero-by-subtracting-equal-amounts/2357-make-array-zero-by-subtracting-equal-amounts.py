class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        non_zero_elements = self.check_non_zeros(nums)
        while 0 not in non_zero_elements and len(non_zero_elements) > 0:
            # print(non_zero_elements)
            elements = self.ele_operation(non_zero_elements)
            count += 1
            non_zero_elements = self.check_non_zeros(elements)
        return count
    
    def ele_operation(self, non_zero_elements):
        min_ele = min(non_zero_elements)
        for index, num in enumerate(non_zero_elements):
            if num > 0:
                non_zero_elements[index] = num - min_ele
        return non_zero_elements
        
    def check_non_zeros(self, nums):
        non_zero = []
        for num in nums:
            if num != 0:
                non_zero.append(num)
        return non_zero
    
