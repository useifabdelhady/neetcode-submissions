from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create list of (value, index) pairs
        arr = [(nums[i], i) for i in range(len(nums))]
        
        # Sort by value (first element of tuple)
        arr.sort()
        
        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = arr[left][0] + arr[right][0]
            
            if current_sum == target:
                return [min(arr[left][1],arr[right][1]),
                        max(arr[left][1],arr[right][1])]
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return []  # No solution (though problem guarantees one)