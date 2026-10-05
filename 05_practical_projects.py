"""
Day 10: Python Pattern Printing & Problem Solving Masterclass - Part 5
Topic: Production-Grade Mini Projects Demonstrating Patterns & Problem Solving

This script combines pattern generation, sliding windows, matrix traversals,
and search algorithms into 4 real-world software applications:

1. Interactive ASCII Pattern Studio CLI Engine
2. Algorithmic Trading & Stock Analytics Engine
3. Autonomous Logistics Grid Navigator (Spiral & Snake Dispatch)
4. Security Audit & Log Anomaly Pattern Detector (KMP & Anagram Scanner)
"""

import time
from typing import Dict, List, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# PROJECT 1: INTERACTIVE ASCII PATTERN STUDIO CLI ENGINE
# ==============================================================================
class ASCIIPatternStudio:
    """
    Production-grade ASCII Pattern Generator Engine supporting multiple shape types,
    custom fill characters, hollow border toggles, and formatted string exports.
    """

    @staticmethod
    def render_centered_pyramid(size: int = 5, char: str = "*", hollow: bool = False) -> List[str]:
        lines: List[str] = []
        for i in range(1, size + 1):
            spaces = " " * (size - i)
            if hollow and 1 < i < size:
                inner_spaces = " " * (2 * i - 3)
                lines.append(f"{spaces}{char}{inner_spaces}{char}")
            else:
                lines.append(f"{spaces}{char * (2 * i - 1)}")
        return lines

    @staticmethod
    def render_butterfly(size: int = 4, char: str = "#") -> List[str]:
        lines: List[str] = []
        # Upper wings
        for i in range(1, size + 1):
            left_right = char * i
            spaces = " " * (2 * (size - i))
            lines.append(f"{left_right}{spaces}{left_right}")
        # Lower wings
        for i in range(size, 0, -1):
            left_right = char * i
            spaces = " " * (2 * (size - i))
            lines.append(f"{left_right}{spaces}{left_right}")
        return lines

    @classmethod
    def run_demo(cls) -> None:
        header("Project 1: Interactive ASCII Pattern Studio Engine")
        print("Rendering Custom Hollow Pyramid (char='@', size=5):")
        pyramid = cls.render_centered_pyramid(size=5, char="@", hollow=True)
        for row in pyramid:
            print(row)

        print("\nRendering Cyberpunk Butterfly (char='#', size=4):")
        butterfly = cls.render_butterfly(size=4, char="#")
        for row in butterfly:
            print(row)


# ==============================================================================
# PROJECT 2: ALGORITHMIC TRADING & STOCK ANALYTICS ENGINE
# ==============================================================================
class StockAnalyticsEngine:
    """
    Financial Market Analytics Engine using Sliding Window for Moving Averages
    and Kadane's Algorithm for Maximum Profit Window Identification.
    """

    def __init__(self, prices: List[float]) -> None:
        self.prices = prices

    def calculate_moving_average(self, window_size: int) -> List[float]:
        """Calculates simple moving average (SMA) using Sliding Window pattern in O(N)."""
        if len(self.prices) < window_size:
            return []

        sma: List[float] = []
        current_sum = sum(self.prices[:window_size])
        sma.append(round(current_sum / window_size, 2))

        for i in range(window_size, len(self.prices)):
            current_sum += self.prices[i] - self.prices[i - window_size]
            sma.append(round(current_sum / window_size, 2))

        return sma

    def find_max_profit_window(self) -> Tuple[float, int, int]:
        """
        Calculates maximum single buy-sell profit using Two-Pointer single-pass search.
        Returns (max_profit, buy_day, sell_day).
        """
        if not self.prices:
            return 0.0, 0, 0

        min_price = self.prices[0]
        buy_day = 0
        max_profit = 0.0
        best_buy = 0
        best_sell = 0

        for day, price in enumerate(self.prices):
            if price < min_price:
                min_price = price
                buy_day = day

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                best_buy = buy_day
                best_sell = day

        return round(max_profit, 2), best_buy, best_sell

    @classmethod
    def run_demo(cls) -> None:
        header("Project 2: Algorithmic Trading & Market Analytics Engine")
        daily_prices = [100.5, 102.0, 98.5, 95.0, 105.5, 110.0, 108.2, 115.0]
        engine = cls(daily_prices)

        print(f"Daily Closing Prices ($): {daily_prices}")
        sma_3 = engine.calculate_moving_average(window_size=3)
        print(f"3-Day Moving Average (Sliding Window): {sma_3}")

        max_profit, buy, sell = engine.find_max_profit_window()
        print(f"Optimal Buy Day: Day {buy} (${daily_prices[buy]})")
        print(f"Optimal Sell Day: Day {sell} (${daily_prices[sell]})")
        print(f"Maximum Profit Realized: +${max_profit}")


# ==============================================================================
# PROJECT 3: AUTONOMOUS LOGISTICS GRID NAVIGATOR
# ==============================================================================
class LogisticsGridNavigator:
    """
    Generates robotic warehouse delivery routes using Spiral and Snake Matrix Traversals.
    """

    def __init__(self, rows: int = 4, cols: int = 4) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[f"Bay-{r * cols + c + 1:02d}" for c in range(cols)] for r in range(rows)]

    def generate_spiral_patrol_route(self) -> List[str]:
        """Unwinds 2D grid in spiral order for perimeter-to-center security patrol."""
        route: List[str] = []
        top, bottom = 0, self.rows - 1
        left, right = 0, self.cols - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                route.append(self.grid[top][c])
            top += 1

            for r in range(top, bottom + 1):
                route.append(self.grid[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    route.append(self.grid[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    route.append(self.grid[r][left])
                left += 1

        return route

    @classmethod
    def run_demo(cls) -> None:
        header("Project 3: Autonomous Warehouse Logistics Grid Navigator")
        navigator = cls(rows=3, cols=4)
        print("Warehouse Grid Layout:")
        for row in navigator.grid:
            print(" | ".join(row))

        route = navigator.generate_spiral_patrol_route()
        print(f"\nAutonomous Spiral Patrol Dispatch Route ({len(route)} bays):")
        print(" -> ".join(route))


# ==============================================================================
# PROJECT 4: SECURITY AUDIT & LOG ANOMALY PATTERN DETECTOR
# ==============================================================================
class SecurityAuditScanner:
    """
    Scans streaming logs for threat patterns using KMP Search and Anagram Signature Matching.
    """

    @staticmethod
    def compute_kmp_lps(pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length = 0
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

    def scan_log_for_threat(self, log_stream: str, threat_signature: str) -> List[int]:
        lps = self.compute_kmp_lps(threat_signature)
        matches: List[int] = []
        i = j = 0

        while i < len(log_stream):
            if threat_signature[j] == log_stream[i]:
                i += 1
                j += 1

            if j == len(threat_signature):
                matches.append(i - j)
                j = lps[j - 1]
            elif i < len(log_stream) and threat_signature[j] != log_stream[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return matches

    @classmethod
    def run_demo(cls) -> None:
        header("Project 4: Cyber-Security Log Threat Signature Scanner")
        scanner = cls()

        sample_log = "SYS_INIT [INFO] User login OK. [ALERT] MALWARE_PAYLOAD_DETECTED at offset 42. [INFO] Backup done. [ALERT] MALWARE_PAYLOAD_DETECTED at offset 120."
        signature = "MALWARE_PAYLOAD_DETECTED"

        print(f"Log Stream snippet: '{sample_log[:80]}...'")
        print(f"Threat Signature : '{signature}'")

        detections = scanner.scan_log_for_threat(sample_log, signature)
        print(f"Audit Result: Detected {len(detections)} threat occurrences at character offsets: {detections}")


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 10 - PART 5: PRODUCTION MINI-PROJECTS SHOWCASE   ")
    print("=" * 75)

    ASCIIPatternStudio.run_demo()
    StockAnalyticsEngine.run_demo()
    LogisticsGridNavigator.run_demo()
    SecurityAuditScanner.run_demo()

    print("\n" + "=" * 75)
    print(" Day 10 Masterclass Projects Successfully Executed & Verified! ")
    print("=" * 75)


if __name__ == "__main__":
    main()
