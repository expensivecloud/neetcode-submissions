class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre_prod = [1] * n
        post_prod = [1] * n

        pre_prod[0] = 1
        post_prod[n - 1] = 1

        for i in range(1, n):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            post_prod[i] = post_prod[i + 1] * nums[i + 1]

        res = [1] * n

        for i in range(n):
            res[i] = pre_prod[i] * post_prod[i]

        return res