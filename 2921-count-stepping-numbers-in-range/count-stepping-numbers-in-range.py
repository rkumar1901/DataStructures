from functools import lru_cache
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        def decrement(number: str):
            """Return number - 1 as a string, or None if number is zero."""
            if number == "0":
                return None

            digits = list(number)
            i = len(digits) - 1

            while digits[i] == "0":
                digits[i] = "9"
                i -= 1

            digits[i] = str(int(digits[i]) - 1)
            result = "".join(digits).lstrip("0")
            return result or "0"

        def count_at_most(bound: str) -> int:
            if bound is None:
                return 0

            digits = list(map(int, bound))

            @lru_cache(None)
            def dp(pos: int, previous: int, tight: bool, started: bool) -> int:
                if pos == len(digits):
                    # Exclude the all-leading-zero representation of 0.
                    return int(started)

                limit = digits[pos] if tight else 9
                total = 0

                for digit in range(limit + 1):
                    next_tight = tight and digit == limit if tight else False

                    if not started and digit == 0:
                        # Still skipping leading zeroes; no adjacency check yet.
                        total += dp(pos + 1, 10, next_tight, False)
                    elif not started or abs(digit - previous) == 1:
                        total += dp(pos + 1, digit, next_tight, True)

                return total % MOD

            return dp(0, 10, True, False)

        below_low = decrement(low)
        return (count_at_most(high) - count_at_most(below_low)) % MOD
