class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.split(" ")
        result = ""
        for i in range(len(s) - 1):
            result += s[i] + "%20"
        result += s[-1]
        return result