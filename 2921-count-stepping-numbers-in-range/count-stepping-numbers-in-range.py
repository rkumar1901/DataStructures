class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:

        MOD = 10**9 + 7

        def count(N):

            if N < 0:
                return 0

            s = str(N)
            n = len(s)

            # dp(pos, prev_digit, tight, started)
            memo = {}

            def dp(pos, prev_digit, tight, started):

                if pos == n:
                    return 1

                key = (pos, prev_digit, tight, started)

                if key in memo:
                    return memo[key]

                limit = int(s[pos]) if tight else 9

                total = 0

                for digit in range(limit + 1):

                    new_tight = tight and digit == limit

                    # Still skipping leading zeros
                    if not started and digit == 0:
                        total += dp(
                            pos + 1,
                            -1,
                            new_tight,
                            False
                        )

                    else:

                        # First real digit
                        if not started:
                            total += dp(
                                pos + 1,
                                digit,
                                new_tight,
                                True
                            )

                        # Next digit must differ by exactly 1
                        elif abs(digit - prev_digit) == 1:
                            total += dp(
                                pos + 1,
                                digit,
                                new_tight,
                                True
                            )

                memo[key] = total % MOD
                return memo[key]

            return dp(0, -1, True, False)

        return (count(int(high)) - count(int(low) - 1)) % MOD
        