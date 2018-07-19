from string import ascii_lowercase


def max_times(string1):
    words = string1.lower()
    return max(ascii_lowercase, key=words.count)


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for s in str:
            if ord('A') <= ord(s) <= ord('Z'):
                # res += chr(ord(s) - ord('A') + ord('a'))
                res += chr(ord(s) + 32)
            else:
                res += s
        return res

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(J.count, S))

    def lengthOfLongestSubstring(self, s):
        """
            给定一个字符串，找出不含有重复字符的最长子串的长度。
            示例：
                给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
                给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
                给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
            思路：

        :type s: str
        :rtype: int
        """
        temp = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            temp = max(i - start + 1, temp)
            d[s[i]] = i
        return temp

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
        """
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1 = 0
        n2 = 0
        for c in num1:
            val = dict[c]
            n1 = n1 * 10 + val
        for s in num2:
            val = dict[s]
            n2 = n2 * 10 + val
        return str(n1 * n2)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # haystack.find(needle)
        if needle == '':
            return 0
        len_n = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                try:
                    if haystack[i:i + len_n] == needle:
                        return i
                except IndexError:
                    pass
        return -1

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = list(s)
        temp.reverse()
        return ''.join(temp)
        # return ''.join(list(s).reverse())

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pass

    def repeatedSubstringPattern(self, s):
        """
        给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
        :type s: str
        :rtype: bool
        """
        tmp = {}
        length = len(s)
        if length < 2:
            return False
        for i in range(len(s)):
            if s[i] in s[0] and i != 0:
                if (s[:i] * (length // i)) == s:
                    return True
            else:
                tmp[s[i]] = i
        return False

    def repeatedSubstringPatternV2(self, s):
        if not s: return False
        s1 = (s + s)[1:-1]
        return s1.find(s) != -1

    def repeatedSubstringPatternV3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]

    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """


solution = Solution()
print(solution.repeatedSubstringPatternV2("aafaaf"))
