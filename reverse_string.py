'''
Example
1:

Input: ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
Example
2:

Input: ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]
'''

s=["h", "e", "l", "l", "o"]
class Solution:
    def reverseString(self, s):
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]
        return s
#lucy = Goose("pilgrim,"lucy","hazel")
#lucy.honk()
test=Solution()

print(test.reverseString(s))

