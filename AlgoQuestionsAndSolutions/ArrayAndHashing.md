# [Two Sum | Leetcode #1](https://leetcode.com/problems/two-sum/description/)

"Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."

## Solution 

### Common approach using a hash table.

Below is one common approach using a hash table (or dictionary) to solve the two-sum problem efficiently:


1. **Initialize a Dictionary (Map):**
   - Create an empty dictionary to store numbers and their indices as you iterate through the list.

2. **Iterate Through the List:**
   - For each element in the array (using its index):
     - **Compute the Complement:**
       - Calculate the difference between the target sum and the current element (i.e., `complement = target - current_number`).
     - **Check for Complement:**
       - Look up the complement in the dictionary:
         - If it exists, you’ve found the two numbers that add up to the target. Return the current index and the stored index of the complement.
     - **Store the Current Element:**
       - If the complement is not found, add the current element and its index to the dictionary.

3. **Handle No-Solution Case:**
   - If you finish the loop without finding a matching pair, then no two numbers add up to the target.

### Complexity Analysis

>- **Time Complexity:** $O(n)$ since it makes a single pass through the list and dictionary lookups are $O(1)$ on average.
>-  **Space Complexity:** $O(n)$.

---

# [Contains Duplicate | Leetcode #217](https://leetcode.com/problems/contains-duplicate/description/)

"Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct."

##  Solutions

### Approach 1: Using a Hash Table (Dictionary)

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

#### Complexity Analysis

>- **Time Complexity:** $O(n)$ on average. Each element is processed once and dictionary operations (lookup and insertion) are $O(1)$ on average.
 >- **Space Complexity:** $O(n)$ in the worst case, where no duplicates are found and the dictionary stores every element.

###  Approach 2: Using a Set

1. **Convert to Set:**
    Convert the list nums into a set. Since a set only stores unique elements, any duplicates in the original list will be removed.
2. **Compare Lengths:**
    -   **Determine Duplicates:**
        Compare the length of the set to the length of the original list.
        -   If the set’s length is less than the list’s length, it indicates that duplicates were removed (i.e., duplicates existed).
        - Otherwise, the lengths are the same, meaning no duplicates were present.
    - **Return the Result:**
        Return the boolean result of whether the lengths differ (i.e., len(set(nums)) != len(nums)).

#### Complexity Analysis
>- **Time Complexity:** $O(n)$. Converting the list to a set involves iterating through all elements, and comparing lengths is $O(1)$.
>- **Space Complexity:** $O(n)$. In the worst case, where no duplicates exist and the set contains all the elements.

---

# [Valid Anagram | Leetcode #242](https://leetcode.com/problems/valid-anagram/description/)

"Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise."

##  Solutions

### Approach 1: Simultaneous Frequency Update.

1. **Input:**
   - Two strings: `s` and `t`.

2. **Length Check:**
   - If the length of `s` is not equal to the length of `t`, then return `false` (they cannot be anagrams).

3. **Initialize Frequency Map:**
   - Create an empty map (or dictionary) to store the frequency difference of characters.

4. **Simultaneous Iteration:**
   - For each index `i` from `0` to `s.length - 1`, perform:
     - **Increment:** Increase the count for the character `s[i]` in the map by 1.
     - **Decrement:** Decrease the count for the character `t[i]` in the map by 1.

5. **Validation of Frequency Map:**
   - Iterate over all values in the frequency map.
   - If any value is not zero, return `false` (indicating a mismatch in character counts).

6. **Output:**
   - If all values in the map are zero, return `true` (the strings are anagrams).

#### Complexity Analysis

>- **Time Complexity:** $O(n)$. Iterating through the strings takes $O(n)$ time, where `n` is the length of the strings. Iterating over the map values (in the worst case, $O(n)$ distinct characters) also takes $O(n)$ time.

>- **Space Complexity:** $O(n)$. The frequency map may store up to $O(n)$ entries in the worst case (if all characters are unique).


### Approach 2: Frequency Dictionary

1. **Initial Length Check:**  
   - Compare the lengths of the two input strings.  
   - **If the lengths differ, return `False`.**

2. **Build Frequency Map for First String:**  
   - Iterate over each character in the first string.  
   - Maintain a dictionary (hash map) to count the frequency of each character.

3. **Validate with Second String:**  
   - For each character in the second string, check if the character exists in the dictionary and has a positive count.  
   - Decrement the count if the check passes.  
   - **If a character is missing or its count is insufficient, return `False`.**

4. **Final Result:**  
   - After processing all characters, if no inconsistencies are found, return `True`.

#### Complexity Analysis
>- **Time Complexity:** $O(n)$, where n is the length of the strings. Building the dictionary and processing the second string both take $O(n)$ time.  


>- **Space Complexity:** In the worst case, each character in the string is unique, resulting in $O(n)$ space. For a fixed-size character set, space is effectively $O(1)$.


### Approach 2: Alternative Using Counter (Python)

1. **Utilize Python's Counter:**  
   - Use the built-in `Counter` from the collections module to count the frequency of characters in both strings.

2. **Direct Comparison:**  
   - Compare the two Counter objects directly.  
   - **Return `True` if they are equal; otherwise, return `False`.**

#### Complexity Analysis
>- **Time Complexity:** Constructing each Counter requires $O(n)$ time.Comparing two Counters takes $O(k)$ time where k is the number of distinct characters (in worst-case, $O(n)$).  

>- **Space Complexity:** Both Counters store counts for each distinct character. $O(n)$ in the worst case, or $O(1)$ for a fixed-size alphabet.

---