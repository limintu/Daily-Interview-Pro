class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        count = {}
        ans = 0

        while j < len(s):
            c = s[j]
            if c in count:
                i = max(i, count[c] + 1)

            ans = max(ans, j - i + 1)
            count[c] = j
            j += 1

        return ans
