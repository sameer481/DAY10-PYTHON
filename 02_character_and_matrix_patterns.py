"""
Day 10: Python Pattern Printing & Problem Solving Masterclass - Part 2
Topic: Character Triangles, Spiral Matrix & 2D Grid Traversal Patterns

This script explores ASCII character manipulations using chr()/ord() arithmetic,
as well as advanced 2D matrix traversal patterns (Spiral, Snake, Concentric Rings).

Patterns Covered in this Script:
1. Character Triangles (Repeating, Sequential, Palindromic Pyramid)
2. Inverted Character Pyramids
3. Clockwise Spiral Matrix Filling (NxN Grid with values 1..N^2)
4. Spiral Matrix Boundary Traversal (Top -> Right -> Bottom -> Left)
5. Snake / Zig-Zag Matrix Row Iteration
6. Concentric Square Layered Pattern (Shrinking numerical borders)
"""

from typing import List, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. ALPHABET & CHARACTER PATTERNS
# ==============================================================================
def print_character_patterns(rows: int = 5) -> None:
    """
    Prints repeating, sequential, and palindromic character patterns using chr() and ord().
    
    ASCII Arithmetic Basics:
    - ord('A') = 65
    - chr(65 + i) produces uppercase letters ('A', 'B', 'C', ...)
    """
    header("1. Alphabet & Character Patterns")

    print(f"--- Repeating Character Triangle (rows={rows}) ---")
    for i in range(rows):
        char = chr(ord('A') + i)
        print((char + " ") * (i + 1))

    print(f"\n--- Sequential Character Triangle (rows={rows}) ---")
    for i in range(1, rows + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        print(" ".join(chars))

    print(f"\n--- Palindromic Character Pyramid (rows={rows}) ---")
    for i in range(1, rows + 1):
        spaces = "  " * (rows - i)
        # Ascending: A..
        ascending = [chr(ord('A') + j) for j in range(i)]
        # Descending: ..A
        descending = [chr(ord('A') + j) for j in range(i - 2, -1, -1)]
        row_str = " ".join(ascending + descending)
        print(f"{spaces}{row_str}")


# ==============================================================================
# 2. SPIRAL MATRIX GENERATION (NxN GRID)
# ==============================================================================
def generate_spiral_matrix(n: int = 5) -> List[List[int]]:
    """
    Generates an N x N matrix filled with numbers 1 to N^2 in clockwise spiral order.
    
    Boundary Pointers Algorithm:
    - Maintain 4 boundary markers: top (0), bottom (n-1), left (0), right (n-1).
    - Step 1: Fill top row from left to right, then top++
    - Step 2: Fill right column from top to bottom, then right--
    - Step 3: Fill bottom row from right to left, then bottom--
    - Step 4: Fill left column from bottom to top, then left++
    - Repeat until top > bottom or left > right.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N^2) for matrix creation.
    """
    header("2. Clockwise Spiral Matrix Filling (N x N)")

    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        # Fill top row (left -> right)
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Fill right column (top -> bottom)
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Fill bottom row (right -> left)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # Fill left column (bottom -> top)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    # Pretty print matrix
    for row in matrix:
        print(" ".join(f"{val:3d}" for val in row))

    return matrix


# ==============================================================================
# 3. SPIRAL MATRIX TRAVERSAL
# ==============================================================================
def traverse_spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Unwinds an arbitrary M x N matrix in spiral order and returns a 1D sequence.
    """
    header("3. Spiral Matrix Traversal Sequence")

    if not matrix or not matrix[0]:
        return []

    result: List[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    print(f"Unwound Spiral Sequence ({len(result)} elements):")
    print(result)
    return result


# ==============================================================================
# 4. SNAKE / ZIG-ZAG MATRIX TRAVERSAL
# ==============================================================================
def print_snake_pattern_matrix(matrix: List[List[int]]) -> None:
    """
    Prints matrix elements in snake/zig-zag order:
    - Row 0 (even): Left -> Right
    - Row 1 (odd) : Right -> Left
    - Row 2 (even): Left -> Right ...
    """
    header("4. Snake / Zig-Zag Matrix Pattern")

    snake_output: List[int] = []
    for r_idx, row in enumerate(matrix):
        if r_idx % 2 == 0:
            # Even row: left to right
            snake_output.extend(row)
        else:
            # Odd row: reversed right to left
            snake_output.extend(reversed(row))

    print("Snake Order Traversal:")
    print(snake_output)


# ==============================================================================
# 5. CONCENTRIC SQUARE LAYERED PATTERN
# ==============================================================================
def print_concentric_square_pattern(n: int = 4) -> None:
    """
    Prints a square matrix of size (2*N - 1) with concentric shrinking number rings.
    
    Example for N=4 (Size = 7x7):
    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4
    
    Formula for cell (i, j):
    Cell value = N - min(i, j, size - 1 - i, size - 1 - j)
    where min distance to any border dictates the layer number!
    """
    header(f"5. Concentric Shrinking Square Rings (N={n})")

    size = 2 * n - 1
    for i in range(size):
        row_vals = []
        for j in range(size):
            # Calculate distance to nearest of the 4 borders
            min_dist = min(i, j, size - 1 - i, size - 1 - j)
            val = n - min_dist
            row_vals.append(f"{val} ")
        print("".join(row_vals))


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 10 - PART 2: CHARACTER & MATRIX TRAVERSAL PATTERNS   ")
    print("=" * 75)

    print_character_patterns(rows=5)
    spiral_mat = generate_spiral_matrix(n=4)
    traverse_spiral_matrix(spiral_mat)
    print_snake_pattern_matrix(spiral_mat)
    print_concentric_square_pattern(n=4)

    print("\n" + "=" * 75)
    print(" Part 2 Complete! Mastered 2D grid boundary indexing & chr/ord math. ")
    print("=" * 75)


if __name__ == "__main__":
    main()
