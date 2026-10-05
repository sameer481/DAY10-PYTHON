"""
Day 10: Python Pattern Printing & Problem Solving Masterclass - Part 4
Topic: Advanced Algorithmic Patterns, Optimizations & Matrix Transformations

This script covers classic computer science optimization algorithms and dynamic state tracking.

Patterns Covered in this Script:
1. Kadane's Algorithm (Max Subarray Sum with Index Tracking)
2. Dutch National Flag Algorithm (3-Way In-Place Partitioning)
3. Knuth-Morris-Pratt (KMP) Substring Pattern Search & LPS Table
4. In-Place 90-Degree Clockwise Matrix Rotation (Transpose + Reverse)
5. Generator-Based Lazy Pattern Streaming (O(1) Auxiliary Memory)
"""

from typing import Generator, List, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. KADANE'S ALGORITHM (MAX SUBARRAY SUM)
# ==============================================================================
def kadanes_algorithm(nums: List[int]) -> Tuple[int, List[int]]:
    """
    Finds the contiguous subarray with the largest sum in O(N) time & O(1) space.
    
    Dynamic Programming State Machine:
    - current_max = max(num, current_max + num)
    - global_max = max(global_max, current_max)
    """
    header("1. Kadane's Algorithm (Maximum Subarray Sum)")

    if not nums:
        return 0, []

    max_so_far = nums[0]
    curr_max = nums[0]

    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > curr_max + nums[i]:
            curr_max = nums[i]
            temp_start = i
        else:
            curr_max += nums[i]

        if curr_max > max_so_far:
            max_so_far = curr_max
            start = temp_start
            end = i

    best_subarray = nums[start : end + 1]
    print(f"Input Array: {nums}")
    print(f"Max Subarray Sum: {max_so_far}")
    print(f"Subarray Range: Index [{start}..{end}] -> {best_subarray}")

    return max_so_far, best_subarray


# ==============================================================================
# 2. DUTCH NATIONAL FLAG ALGORITHM (3-WAY PARTITIONING)
# ==============================================================================
def dutch_national_flag_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array containing only 0s, 1s, and 2s in a single pass O(N) time
    and O(1) auxiliary space using 3 pointers: low, mid, high.
    
    Rules:
    - Everything to the left of low is 0.
    - Everything to the right of high is 2.
    - Everything between low and mid-1 is 1.
    """
    header("2. Dutch National Flag (3-Way In-Place Partitioning)")

    print(f"Before Sorting: {arr}")
    low, mid = 0, 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    print(f"After Sorting : {arr}")
    return arr


# ==============================================================================
# 3. KMP PATTERN MATCHING & LPS TABLE
# ==============================================================================
def build_lps_array(pattern: str) -> List[int]:
    """Builds the Longest Prefix Suffix (LPS) lookup table for KMP algorithm."""
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_pattern_search(text: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt (KMP) String Matching Algorithm.
    Achieves O(N + M) time complexity instead of naive O(N * M).
    """
    header(f"3. KMP Pattern Search ('{pattern}' in '{text}')")

    lps = build_lps_array(pattern)
    print(f"Precomputed LPS Table for pattern '{pattern}': {lps}")

    matches: List[int] = []
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            match_idx = i - j
            matches.append(match_idx)
            print(f"-> Pattern match found at index {match_idx}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


# ==============================================================================
# 4. IN-PLACE 90-DEGREE CLOCKWISE MATRIX ROTATION
# ==============================================================================
def rotate_matrix_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotates an N x N matrix 90 degrees clockwise in-place with O(1) extra space.
    
    Transformation Formula:
    1. Transpose matrix: Swap matrix[i][j] with matrix[j][i].
    2. Reverse each row left-to-right.
    """
    header("4. In-Place 90-Degree Clockwise Matrix Rotation")

    n = len(matrix)
    print("Original Matrix:")
    for row in matrix:
        print(row)

    # Step 1: Transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse rows
    for row in matrix:
        row.reverse()

    print("\nRotated 90° Clockwise Matrix:")
    for row in matrix:
        print(row)

    return matrix


# ==============================================================================
# 5. LAZY PATTERN GENERATOR STREAMING
# ==============================================================================
def generate_pyramid_stream(rows: int) -> Generator[str, None, None]:
    """
    Generator function that streams pattern lines on demand.
    Reduces memory consumption to O(1) auxiliary memory for huge patterns.
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        yield f"{spaces}{stars}"


def demonstrate_generator_pattern() -> None:
    header("5. Lazy Pattern Streaming Generator (O(1) Memory)")

    print("Streaming 5 rows of Centered Pyramid dynamically:")
    for line in generate_pyramid_stream(5):
        print(line)


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 10 - PART 4: ADVANCED ALGORITHMIC PATTERNS & ROTATIONS   ")
    print("=" * 75)

    sample_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    kadanes_algorithm(sample_arr)

    dnf_arr = [2, 0, 2, 1, 1, 0, 1, 2, 0]
    dutch_national_flag_sort(dnf_arr)

    kmp_pattern_search("ABABDABACDABABCABAB", "ABABCABAB")

    square_mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix_90_clockwise(square_mat)

    demonstrate_generator_pattern()

    print("\n" + "=" * 75)
    print(" Part 4 Complete! Mastered Kadane, DNF, KMP, and Matrix Transposition. ")
    print("=" * 75)


if __name__ == "__main__":
    main()
