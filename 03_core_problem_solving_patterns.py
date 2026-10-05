"""
Day 10: Python Pattern Printing & Problem Solving Masterclass - Part 3
Topic: Core Algorithmic Problem-Solving Design Patterns

This script details fundamental design patterns that form the backbone of modern
software engineering interviews and production system optimizations.

Patterns Covered in this Script:
1. Two-Pointer Converging & Parallel Patterns
2. Sliding Window (Fixed Size & Variable Size Window)
3. Fast & Slow Pointers (Floyd's Cycle Detection)
4. Hash Map Frequency Counter Pattern
5. Prefix Sum Array & Range Query Optimization
"""

from typing import Dict, List, Optional, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. TWO-POINTER PATTERN
# ==============================================================================
def two_pointer_target_sum(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Finds two numbers in a SORTED array that add up to 'target' in O(N) time.
    
    Algorithm:
    - Left pointer at index 0, Right pointer at index len(arr)-1.
    - If sum == target, return indices.
    - If sum < target, left++ (to increase sum).
    - If sum > target, right-- (to decrease sum).
    
    Time Complexity: O(N) linear time (compared to O(N^2) brute force nested loop).
    Space Complexity: O(1) auxiliary space.
    """
    header("1. Two-Pointer Pattern (Sorted Pair Sum)")

    left, right = 0, len(arr) - 1
    iterations = 0

    while left < right:
        iterations += 1
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print(f"Match found in {iterations} iterations: arr[{left}] ({arr[left]}) + arr[{right}] ({arr[right]}) = {target}")
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    print("No pair found matching target.")
    return None


# ==============================================================================
# 2. SLIDING WINDOW PATTERN
# ==============================================================================
def sliding_window_max_sum(arr: List[int], k: int) -> Tuple[int, List[int]]:
    """
    Finds the maximum sum of any contiguous subarray of fixed size 'k'.
    
    Sliding Window Technique:
    - Calculate sum of first window (elements 0 to k-1).
    - Slide window right by 1 element: new_sum = old_sum + arr[i] - arr[i-k].
    
    Time Complexity: O(N) single pass!
    Space Complexity: O(1) space.
    """
    header(f"2. Sliding Window Pattern (Max Sum Subarray of size K={k})")

    if len(arr) < k:
        raise ValueError("Array length must be >= k")

    # Step 1: Sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    best_start_idx = 0

    # Step 2: Slide the window across array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add incoming, subtract outgoing
        if window_sum > max_sum:
            max_sum = window_sum
            best_start_idx = i - k + 1

    best_subarray = arr[best_start_idx : best_start_idx + k]
    print(f"Array: {arr}")
    print(f"Max Sum Subarray of size {k}: {best_subarray} -> Max Sum = {max_sum}")
    return max_sum, best_subarray


def sliding_window_longest_unique_substring(s: str) -> int:
    """
    Dynamic Variable-Size Sliding Window:
    Finds the length of the longest substring without repeating characters.
    """
    print(f"\n--- Dynamic Window: Longest Substring Without Repeating Chars ('{s}') ---")
    char_index_map: Dict[str, int] = {}
    left = 0
    max_len = 0
    best_substr = ""

    for right, char in enumerate(s):
        # If character was seen and is inside the current window, move left pointer
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        
        char_index_map[char] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            best_substr = s[left : right + 1]

    print(f"Longest Substring: '{best_substr}' (Length: {max_len})")
    return max_len


# ==============================================================================
# 3. FAST & SLOW POINTERS (FLOYD'S CYCLE DETECTION)
# ==============================================================================
def find_duplicate_floyd(nums: List[int]) -> int:
    """
    Finds duplicate number in array of N+1 integers (values between 1 and N)
    using Floyd's Tortoise and Hare Cycle Detection Algorithm.
    
    Time Complexity: O(N)
    Space Complexity: O(1) in-place without modifying array!
    """
    header("3. Fast & Slow Pointers (Floyd's Tortoise & Hare Cycle Detection)")

    # Phase 1: Finding the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to the cycle (the duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    print(f"Array containing duplicate: {nums}")
    print(f"Detected Duplicate Number via Floyd's Algorithm: {slow}")
    return slow


# ==============================================================================
# 4. FREQUENCY MAP PATTERN
# ==============================================================================
def is_valid_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams using O(N) Hash Map frequency counts.
    """
    header(f"4. Frequency Map Pattern (Anagram Check: '{s1}' vs '{s2}')")

    if len(s1) != len(s2):
        print("Length mismatch -> Not Anagrams.")
        return False

    freq: Dict[str, int] = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1

    for char in s2:
        if char not in freq or freq[char] == 0:
            print(f"Character '{char}' count mismatch -> Not Anagrams.")
            return False
        freq[char] -= 1

    print("Result: Valid Anagrams! (Frequency mapping identical)")
    return True


# ==============================================================================
# 5. PREFIX SUM & RANGE QUERY OPTIMIZATION
# ==============================================================================
class PrefixSumEngine:
    """
    Precomputes prefix sum array in O(N) time to answer range sum queries in O(1) time.
    
    Formula:
    prefix[0] = 0
    prefix[i] = prefix[i-1] + arr[i-1]
    
    Range Sum Query(L, R) = prefix[R + 1] - prefix[L]
    """

    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        self.prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def query(self, left: int, right: int) -> int:
        """Query sum of subsegment arr[left..right] in O(1) constant time."""
        if left < 0 or right >= len(self.arr) or left > right:
            raise IndexError("Invalid query indices")
        return self.prefix[right + 1] - self.prefix[left]


def demonstrate_prefix_sum() -> None:
    header("5. Prefix Sum Array & O(1) Range Query Engine")

    data = [10, 20, -5, 15, 30, 8, 12]
    engine = PrefixSumEngine(data)

    print(f"Original Array: {data}")
    print(f"Precomputed Prefix Array: {engine.prefix}")

    # Query sum from index 1 to 4 (values: 20 + -5 + 15 + 30 = 60)
    q1 = engine.query(1, 4)
    print(f"Query Range [1..4] Sum: {q1} (Calculated in O(1) time)")

    # Query sum from index 0 to 6 (full array sum)
    q2 = engine.query(0, 6)
    print(f"Query Range [0..6] Total Sum: {q2} (Calculated in O(1) time)")


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 10 - PART 3: CORE PROBLEM SOLVING PATTERNS IN PYTHON   ")
    print("=" * 75)

    sorted_arr = [2, 7, 11, 15, 22, 35, 40]
    two_pointer_target_sum(sorted_arr, target=37)

    arr_data = [2, 1, 5, 1, 3, 2, 9, 7, 1]
    sliding_window_max_sum(arr_data, k=3)
    sliding_window_longest_unique_substring("abcabcbb")

    duplicate_arr = [1, 3, 4, 2, 2]
    find_duplicate_floyd(duplicate_arr)

    is_valid_anagram("listen", "silent")

    demonstrate_prefix_sum()

    print("\n" + "=" * 75)
    print(" Part 3 Complete! Mastered Two-Pointer, Windowing & Hash Map patterns. ")
    print("=" * 75)


if __name__ == "__main__":
    main()
