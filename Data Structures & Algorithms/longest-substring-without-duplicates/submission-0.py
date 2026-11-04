class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        counter = {}
        
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            while counter[s[r]] > 1:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, r - left + 1)

        return longest