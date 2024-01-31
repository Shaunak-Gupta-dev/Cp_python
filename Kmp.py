# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# optimization over naive string matching.
# watch abdul bari video for the explanation(god level): https://www.youtube.com/watch?v=V5-7GzOfADQ
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
