from typing import List
from collections import Counter


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

    def valid_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        for c in s:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1

        for c in t:
            if c in char_map and char_map[c] > 0:
                char_map[c] -= 1
            else:
                return False

        return True

    def valid_anagram_alternative(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
