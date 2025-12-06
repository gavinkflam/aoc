"""Solution for 2025 star 4.

Problem page:
    https://adventofcode.com/2025/day/2

Solutions:
    1. Brute force
        - O(nm * log^2(m)) time, O(1) auxiliary space,
            where n = number of ranges,
                  m = maximum number
    2. Composition + hash set
        - O(n * (10 ** (log10(m) / 2))) time, O(m) auxiliary space
"""

from aoclibs import inputs2


def run(ranges: list[list[str]]) -> int:
    """Find the sum of the invalid IDs."""
    ans = 0

    for lo_str, hi_str in ranges:
        lo, hi = int(lo_str), int(hi_str)
        lo_len, hi_len = len(lo_str), len(hi_str)

        i = 1
        min_id = 11
        seen = set()

        while min_id <= hi:
            i_str = str(i)
            i_len = len(i_str)

            min_freqs = max(2, (lo_len + i_len - 1) // i_len)
            max_freqs = hi_len // i_len

            for freq in range(min_freqs, max_freqs + 1):
                val = int(i_str * freq)

                if lo <= val <= hi and val not in seen:
                    seen.add(val)
                    ans += val

            i += 1
            min_id = int(str(i) * 2)

    return ans


PARSER = inputs2.compose(inputs2.mapf(inputs2.splitf("-")), inputs2.splitf(","))
PRINTER = str
