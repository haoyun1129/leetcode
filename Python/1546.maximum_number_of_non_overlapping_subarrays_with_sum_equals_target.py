from functools import lru_cache
from typing import List, Tuple


class Solution:
    """
    https://leetcode.com/contest/weekly-contest-201/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
    Notice that the number would be negative
    """

    def __init__(self):
        self.maxNonOverlapping = self.dp_map_prefix

    # DP/Map/Prefix - O(N)
    # TODO: Understand https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/780882/Java-14-lines-Greedy-PrefixSum-with-line-by-line-explanation-easy-to-understand
    def dp_map_prefix(self, nums: List[int], target: int) -> int:
        res, sum = 0, 0
        dic = dict()
        dic[0] = 0
        for i, n in enumerate(nums):
            sum += n
            print(i, n, "sum", sum)
            if (sum - target) in dic:
                res = max(res, dic[sum-target] + 1)
            dic[sum] = res
            print("res", res, dic)
        return res

    # TLE & maximum recursion depth exceeded in comparison
    def dp_resursive(self, nums: List[int], target: int) -> int:
        # print("maxNonOverlapping", nums, target)
        @lru_cache(maxsize=None)
        def helper(nums: Tuple[int]):
            nonlocal target
            cur_max = 0
            if sum(nums) == target:
                cur_max = 1
            for i in range(1, len(nums)):
                m = helper(nums[:i]) + helper(nums[i:])
                if m > cur_max:
                    cur_max = m
            return cur_max

        return helper(tuple(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))  # 2
    # print(s.maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))  # 2
    # print(s.maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))  # 3
    # print(s.maxNonOverlapping(nums=[0, 0, 0], target=0))  # 3
    # print(s.maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], 6))  # 2

    # print(s.maxNonOverlapping(
    #     [1, 3, 2, -1, 3, 1, 0, 0, 3, 1, 0, 3, 2, 1, 3, -1, 1, -1, 3, 3, 0, 3, 1, 0, 3, -1, 0, 2, 2, -1, 0], 4))  # 7
    # print(s.maxNonOverlapping([2, 1, 1, -2, -3, -2, -2, 1, 3, 1], 2))  # 3
    # print(s.maxNonOverlapping(
    #     [1, 3, 2, -1, 3, 1, 0, 0, 3, 1, 0, 3, 2, 1, 3, -1, 1, -1, 3, 3, 0, 3, 1, 0, 3, -1, 0, 2, 2, -1, 0], 4))

    # maximum recursion depth exceeded in comparison
    # print(s.maxNonOverlapping(
    #     [18, 11, 0, 30, 3, 20, 8, -6, 0, 0, 0, -9, 29, 4, 10, 6, 17, 24, 7, 27, -9, 11, 8, 5, 6, 21, 0, 27, 4, 24, -5,
    #      2, -2, 0, 12, 7, 9, 14, 26, 6, -5, -1, -4, 8, 7, -3, 2, 4, -8, 8, 2, 17, 12, 23, 24, 18, 20, 10, 4, 21, 18, 21,
    #      -8, 2, 9, 5, -5, 9, 9, 22, -8, -6, -3, 20, -2, 30, -9, 7, -7, 10, 16, 0, 29, 11, 4, 11, -8, 13, 18, -5, 20, 27,
    #      -8, 22, 15, -2, -8, 8, 22, 0, 28, 11, 29, 26, 15, 7, -2, 26, -2, 16, -2, 7, 2, 23, -3, 30, 21, 6, 24, 20, 20,
    #      28, 8, 30, 16, 3, 15, -5, 1, 23, -6, -5, 19, -2, -2, 9, 30, 17, 26, 1, 8, 15, 25, 6, 18, 9, -5, 2, 23, 21, 17,
    #      15, 21, 13, -2, 10, 19, 23, 0, -3, 5, 25, 0, -8, 0, -2, -2, 20, -4, 29, -7, 2, 26, 30, 4, 5, 30, 16, -1, 0, 24,
    #      18, 13, 3, 19, 20, -6, 26, 24, 0, 22, 23, -8, 28, 7, 16, 27, 23, 20, 18, 10, -3, 2, 15, 22, 26, -4, 15, 29, 19,
    #      17, 28, -9, -2, 27, 22, 10, 19, 30, 0, 15, 27, -6, -5, 15, -3, -9, 14, -4, -6, 24, -3, 4, 17, 0, 25, 3, 4, 9,
    #      26, -8, 21, 7, 30, 18, 24, 2, -4, 14, 14, 26, -1, 19, 18, 25, -6, 16, 19, 5, 12, 25, -10, 9, 3, 21, 30, -10,
    #      -4, 3, 18, 14, 7, -10, 3, 25, 23, 26, 9, 12, -9, 30, -10, 12, 10, 22, 12, 0, 8, 0, 26, -1, 13, 17, 16, 2, 18,
    #      3, 12, 12, 23, 23, -4, 19, -7, 14, 17, 2, 4, 30, 10, 0, 7, -7, 18, 5, 15, 5, 16, 17, 22, -9, 29, 8, 28, 5, 11,
    #      8, 14, -5, 14, 1, 16, 25, 4, 5, -3, 2, 20, -2, 0, 5, 27, 5, 22, 3, 6, 12, -8, 26, -10, 20, 8, 23, 2, 19, -4, 9,
    #      19, -9, 27, -9, 8, 25, 8, 21, 29, 20, 19, -1, 14, -1, 10, 8, 8, 24, 30, 15, 5, 30, 16, 25, -4, 19, 10, 5, 22,
    #      17, 18, 21, 3, -4, 11, 25, 10, 15, 15, 26, 10, -6, -5, -9, 5, 15, 0, 28, 20, 11, 22, 18, 25, 21, 6, 20, 18, 11,
    #      6, -1, -6, 10, 29, 15, 7, 19, 1, 28, 22, 13, 16, 14, 27, 7, 18, 20, -7, 27, 26, 7, 1, 11, 14, 18, -3, 27, 13,
    #      10, 26, 12, -4, 0, -5, 19, 12, 28, 4, 30, 30, 6, 11, 22, 11, 20, 4, 16, -7, 8, 27, 11, -10, -8, 24, 0, -1, 30,
    #      28, 14, 0, -6, -6, -5, 12, 13, 11, -10, 25, -1, -4, 13, 5, 5, -7, 3, 25, -3, 27, 14, -4, 15, -3, 28, 6, 27, 5,
    #      8, 28, -4, 13, 9, 14, -2, -6, -7, 11, 18, -6, 3, -3, 3, 30, 22, 17, 5, 9, 3, 23, 27, -9, 13, 28, 6, -4, 6, 26,
    #      24, 14, 4, -8, 22, -3, 26, 10, -2, 13, -2, 11, 13, -9, 17, 18, 15, -10, 15, 18, -10, 5, 13, 11, -10, 12, 15,
    #      20, 7, 10, -10, 13, 27, -10, 5, 10, 19, 22, -7, -5, 4, 12, 9, 14, 17, -7, -9, 26, 9, 29, 21, 19, 30, -8, -10,
    #      21, 17, -7, 16, -3, 20, 27, -5, 20, -9, 11, 20, 28, 15, 18, 18, 8, 26, 12, 22, 16, -3, 16, 3, 17, -7, 18, 26,
    #      -4, 25, 5, -3, 14, -2, 14, 27, -9, 13, 8, 15, 20, 27, 23, -9, 21, 14, 29, -8, 19, -4, -1, 3, 14, 24, 15, 9, 23,
    #      4, 12, 11, 7, 8, 19, 19, 4, 11, 29, 28, 23, -1, 30, 15, 19, 2, 26, -4, 9, 12, -4, 8, 10, 25, 3, 21, 11, 14, 20,
    #      26, 26, 14, 13, 25, -5, 8, 30, 18, -8, 29, -3, 14, -10, 20, 20, 3, 7, -6, -6, 12, 28, 24, 21, 1, -9, 22, -6,
    #      -8, -1, 9, 6, 13, 8, -9, 21, 3, 1, 9, -7, -1, 20, 9, 3, 30, 20, 21], 28))
