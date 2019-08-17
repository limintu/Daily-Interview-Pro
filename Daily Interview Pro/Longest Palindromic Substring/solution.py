class Solution:
    def longestPalindrome(self, s: str):
        ans = ""
        for i, c in enumerate(s):
            candidate1 = self.search(s, i, i)
            candidate2 = ""
            if i + 1 < len(s) and s[i] == s[i+1]:
                candidate2 = self.search(s, i, i + 1)

            ans = candidate1 if len(ans) < len(candidate1) else ans
            ans = candidate2 if len(ans) < len(candidate2) else ans
        return ans

    def search(self, s: str, l: int, r: int) -> str:
        while l - 1 >= 0 and r + 1 < len(s):
            if s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            else:
                break

        return s[l:r+1]
