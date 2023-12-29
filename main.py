# find the longest palindrome substirng form a give sub-string
# for example string = "kebede"  so the answer is going to be ebe or ede
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resleng = 0
        for i in range(len(s)):
            # odd length
            L, r = i, i
            while L >= 0 and r < len(s) and s[L] == s[r]:
                if (r - L + 1) > resleng:
                    res = s[L:r + 1]
                    resleng = r - L + 1
                L -= 1
                r += 1

                # even length
            L, r = i, i + 1
            while L >= 0 and r < len(s) and s[L] == s[r]:
                if (r - L + 1) > resleng:
                    res = s[L:r + 1]
                    resleng = r - L + 1
                L -= 1
                r += 1
        return res
string = "kebede"
answer = Solution()
final = answer.longestPalindrome(string)
print(final)

