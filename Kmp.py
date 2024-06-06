# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# optimization over naive string matching.

haystack = 'abcdeaabcdaa'
needle = 'aabc'
s = needle + '#' + haystack
def strStr(s):
    lps = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        pre = lps[i-1]
        while pre > 0 and s[i] != s[pre]:
            pre = lps[pre-1]
        lps[i] = pre + (1 if s[i] == s[pre] else 0)
    return lps

lps = strStr(s)

for i in range(len(lps)):
    if lps[i] == len(needle):
        print(i - 2*len(needle))
        