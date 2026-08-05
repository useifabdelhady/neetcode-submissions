class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         res = cnt = 0
         for num in nums:
            if num == 0:
                res = max(cnt,res)
                cnt = 0
            else:
                cnt += 1
         return max(cnt,res)
        