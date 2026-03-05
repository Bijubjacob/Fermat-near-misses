
from collections import Counter

def count_permutations(text: str, pattern: str) -> int:
    if len(pattern) > len(text):
        return 0

    pattern_count = Counter(pattern)
    window_count = Counter()

    left = 0
    matches = 0

    for right in range(len(text)):
        # Add current character to window
        window_count[text[right]] += 1

        # Maintain window size
        if right - left + 1 > len(pattern):
            window_count[text[left]] -= 1
            if window_count[text[left]] == 0:
                del window_count[text[left]]
            left += 1

        # Check match
        if right - left + 1 == len(pattern):
            if window_count == pattern_count:
                matches += 1

    return matches

