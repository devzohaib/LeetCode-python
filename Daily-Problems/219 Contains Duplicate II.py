from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # empty dictionary
        map = dict()
        # iterate over the list with index
        for i, num in enumerate(nums):
            # apply both conditions at once
            if num in map and abs(i - map[num]) <= k:
                return True
            # else add it to the dictionary
            else:
                map[num] = i
        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))
