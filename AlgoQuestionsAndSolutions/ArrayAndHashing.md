## [Two Sum | Leetcode #1](https://leetcode.com/problems/two-sum/description/)

"Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."

### Solution 

Below is one common approach using a hash table (or dictionary) to solve the two-sum problem efficiently:

1. **Initialize a Dictionary (Map):**
Create an empty dictionary to store numbers and their indices as you iterate through the list.
2. **Iterate Through the List:**
For each element in the array (using its index):
    - **Compute the Complement:**
Calculate the difference between the target sum and the current element (i.e., complement = target - current_number).
    - **Check for Complement:**
    Look up the complement in the dictionary:
        - If it exists, you’ve found the two numbers that add up to the target. Return the current index and the stored index of the complement.
    - **Store the Current Element:**
If the complement is not found, add the current element and its index to the dictionary.
3. **Handle No-Solution Case:**
If you finish the loop without finding a matching pair, then no two numbers add up to the target.

>- This method runs in O(n) time and uses O(n) space, since it makes a single pass through the list and dictionary lookups are O(1) on average.

---

## [Contains Duplicate | Leetcode #217](https://leetcode.com/problems/contains-duplicate/description/)

"Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct."

### Solution

#### Using a Hash Table (Dictionary)

1.	**Initialize Data Structure:**
    Create an empty dictionary called seen to track numbers you’ve encountered.
2. **Iterate Through Each Number:**
    For every number num in the list nums:
    - **Check for Duplicate:**
        If num already exists as a key in seen, then a duplicate is found.
        - **Return True:**
            Immediately return True since a duplicate exists.
    - **Store the Number:**
        If num is not in seen, add it as a key with an arbitrary value (e.g., True) to indicate it has been seen.
3. **Conclude the Check:**
    If the loop completes without finding any duplicate, return False indicating that no duplicates were found.

>- Time Complexity:
    O(n) on average.
    Each element is processed once and dictionary operations (lookup and insertion) are O(1) on average.
 >- Space Complexity:
    O(n) in the worst case, where no duplicates are found and the dictionary stores every element.

#### Alternative Solution: Using a Set

1. **Convert to Set:**
    Convert the list nums into a set. Since a set only stores unique elements, any duplicates in the original list will be removed.
2. **Compare Lengths:**
    -   **Determine Duplicates:**
        Compare the length of the set to the length of the original list.
        -   If the set’s length is less than the list’s length, it indicates that duplicates were removed (i.e., duplicates existed).
        - Otherwise, the lengths are the same, meaning no duplicates were present.
    - **Return the Result:**
        Return the boolean result of whether the lengths differ (i.e., len(set(nums)) != len(nums)).

>- Time Complexity: O(n).
    Converting the list to a set involves iterating through all elements, and comparing lengths is O(1).
>- Space Complexity: O(n).
	In the worst case, where no duplicates exist and the set contains all the elements.