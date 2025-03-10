from typing import List


class ArrayAndHashing:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [num_map[target - nums[i]], i]
            num_map[nums[i]] = i
        return []

    def contains_duplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False

    def contains_duplicate_alternative(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
