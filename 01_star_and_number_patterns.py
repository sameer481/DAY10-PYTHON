"""
Day 10: Python Pattern Printing & Problem Solving Masterclass - Part 1
Topic: Star Shapes, Geometry & Number Patterns with Neat Explanations

Pattern printing exercises build core mastery over nested loops, index arithmetic,
spatial reasoning, space padding calculation, and loop invariant control.

Patterns Covered in this Script:
1. Right-Angled Triangle & Inverted Right-Angled Triangle (Star)
2. Centered Pyramid & Inverted Centered Pyramid (Star)
3. Solid & Hollow Diamond Patterns (Star)
4. Hourglass & Butterfly Patterns (Star)
5. Sequential & Inverted Number Triangles
6. Floyd's Triangle & Binary Alternating Pattern
7. Palindromic Number Pyramid
8. Pascal's Triangle (Combinatoric nCr & Dynamic Iterative methods)
"""

from typing import List


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. BASIC & INVERTED STAR TRIANGLES
# ==============================================================================
def print_right_angled_triangles(rows: int = 5) -> None:
    """
    Demonstrates standard and inverted right-angled star triangles.
    
    Logic & Formula:
    - Standard: For row i (1 to N), print i stars.
    - Inverted: For row i (1 to N), print (N - i + 1) stars.
    
    Time Complexity: O(N^2) total characters printed.
    Space Complexity: O(1) auxiliary space.
    """
    header("1. Right-Angled & Inverted Right-Angled Triangles")

    print(f"--- Standard Right-Angled Triangle (rows={rows}) ---")
    # Row loop from 1 to rows inclusive
    for i in range(1, rows + 1):
        # Repeat '*' i times
        print("*" * i)

    print(f"\n--- Inverted Right-Angled Triangle (rows={rows}) ---")
    # Row loop from rows down to 1
    for i in range(rows, 0, -1):
        print("*" * i)

    print(f"\n--- Right-Aligned Triangle (rows={rows}) ---")
    # For row i, leading spaces = (rows - i), stars = i
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * i
        print(f"{spaces}{stars}")


# ==============================================================================
# 2. CENTERED PYRAMIDS & INVERTED PYRAMIDS
# ==============================================================================
def print_centered_pyramids(rows: int = 5) -> None:
    """
    Demonstrates centered pyramid and inverted pyramid patterns.
    
    Mathematical Relations for Row i (1-indexed):
    - Leading spaces: (N - i)
    - Stars in Pyramid: (2 * i - 1)
    
    Example for N=3:
    Row 1: spaces=2, stars=1  -> "  *"
    Row 2: spaces=1, stars=3  -> " ***"
    Row 3: spaces=0, stars=5  -> "*****"
    """
    header("2. Centered Pyramid & Inverted Pyramid")

    print(f"--- Solid Centered Star Pyramid (rows={rows}) ---")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

    print(f"\n--- Inverted Centered Star Pyramid (rows={rows}) ---")
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")


# ==============================================================================
# 3. SOLID & HOLLOW DIAMOND PATTERNS
# ==============================================================================
def print_diamond_patterns(n: int = 5) -> None:
    """
    Demonstrates solid diamond and hollow diamond patterns.
    
    Solid Diamond Logic:
    - Upper pyramid: i from 1 to n
    - Lower pyramid: i from n-1 down to 1
    
    Hollow Diamond Logic:
    - Row 1 & Row 2n-1: single star surrounded by spaces.
    - Middle rows: leading spaces, first '*', inner spaces (2*i - 3), second '*'.
    """
    header("3. Solid & Hollow Diamond Patterns")

    print(f"--- Solid Star Diamond (n={n}) ---")
    # Upper half including middle
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    print(f"\n--- Hollow Star Diamond (n={n}) ---")
    # Upper half
    for i in range(1, n + 1):
        spaces_outer = " " * (n - i)
        if i == 1:
            print(f"{spaces_outer}*")
        else:
            spaces_inner = " " * (2 * i - 3)
            print(f"{spaces_outer}*{spaces_inner}*")
    # Lower half
    for i in range(n - 1, 0, -1):
        spaces_outer = " " * (n - i)
        if i == 1:
            print(f"{spaces_outer}*")
        else:
            spaces_inner = " " * (2 * i - 3)
            print(f"{spaces_outer}*{spaces_inner}*")


# ==============================================================================
# 4. HOURGLASS & BUTTERFLY PATTERNS
# ==============================================================================
def print_hourglass_and_butterfly(n: int = 4) -> None:
    """
    Demonstrates Hourglass and Butterfly geometrical patterns.
    
    Hourglass: Inverted Pyramid followed by Upper Pyramid.
    Butterfly: Left wing + Inner spaces + Right wing.
    """
    header("4. Hourglass & Butterfly Patterns")

    print(f"--- Star Hourglass Pattern (n={n}) ---")
    # Upper inverted pyramid
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower pyramid (skipping 1 star center to maintain symmetric hourglass)
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    print(f"\n--- Butterfly Pattern (n={n}) ---")
    # Upper wings
    for i in range(1, n + 1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(f"{stars}{spaces}{stars}")
    # Lower wings
    for i in range(n, 0, -1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(f"{stars}{spaces}{stars}")


# ==============================================================================
# 5. NUMBER PATTERNS: FLOYD'S & BINARY PATTERNS
# ==============================================================================
def print_number_and_floyds_triangle(rows: int = 5) -> None:
    """
    Demonstrates Floyd's Triangle and Binary Alternating Triangles.
    
    Floyd's Triangle:
    - Numbers increment continuously across row boundaries:
      1
      2 3
      4 5 6
      7 8 9 10
      
    Binary Alternating Pattern:
    - Alternates starting digit per row (1 for odd rows, 0 for even rows).
    """
    header("5. Floyd's Triangle & Binary Alternating Pattern")

    print(f"--- Floyd's Triangle (rows={rows}) ---")
    num = 1
    for i in range(1, rows + 1):
        row_str = ""
        for j in range(i):
            row_str += f"{num:<3}"
            num += 1
        print(row_str)

    print(f"\n--- Binary Alternating Triangle (rows={rows}) ---")
    for i in range(1, rows + 1):
        # Start digit: 1 if row is odd, 0 if row is even
        start = 1 if i % 2 != 0 else 0
        row_vals = []
        for j in range(i):
            row_vals.append(str(start))
            start = 1 - start  # Toggle between 1 and 0
        print(" ".join(row_vals))


# ==============================================================================
# 6. PALINDROMIC NUMBER PYRAMID
# ==============================================================================
def print_palindromic_number_pyramid(rows: int = 5) -> None:
    """
    Prints a symmetrical palindromic number pyramid.
    
    Row 1:     1
    Row 2:    121
    Row 3:   12321
    Row 4:  1234321
    Row 5: 123454321
    
    Logic:
    - Space padding: (rows - i)
    - Ascending sequence: 1 to i
    - Descending sequence: (i - 1) down to 1
    """
    header("6. Palindromic Number Pyramid")

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        # Ascending sequence
        ascending = [str(x) for x in range(1, i + 1)]
        # Descending sequence
        descending = [str(x) for x in range(i - 1, 0, -1)]
        row_str = "".join(ascending + descending)
        print(f"{spaces}{row_str}")


# ==============================================================================
# 7. PASCAL'S TRIANGLE
# ==============================================================================
def generate_pascals_triangle(n: int = 6) -> List[List[int]]:
    """
    Generates and formats Pascal's Triangle up to 'n' rows.
    
    Pascal's Principle:
    - Every row starts and ends with 1.
    - Value at triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c].
    - Alternatively via Combinatorics: C(n, k) = n! / (k! * (n - k)!).
    
    Time Complexity: O(N^2)
    Space Complexity: O(N^2) to store triangle structure.
    """
    header("7. Pascal's Triangle (Dynamic Iterative Approach)")

    triangle: List[List[int]] = []

    for i in range(n):
        row = [1] * (i + 1)
        # Calculate inner elements from previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    # Centered pretty printing
    max_width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        row_formatted = "   ".join(map(str, row))
        print(row_formatted.center(max_width))

    return triangle


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 10 - PART 1: STAR & NUMBER PATTERN PRINTING MASTERCLASS   ")
    print("=" * 75)

    print_right_angled_triangles(rows=5)
    print_centered_pyramids(rows=5)
    print_diamond_patterns(n=4)
    print_hourglass_and_butterfly(n=4)
    print_number_and_floyds_triangle(rows=5)
    print_palindromic_number_pyramid(rows=5)
    generate_pascals_triangle(n=6)

    print("\n" + "=" * 75)
    print(" Part 1 Complete! Mastered nested loop spatial reasoning & arithmetic. ")
    print("=" * 75)


if __name__ == "__main__":
    main()
