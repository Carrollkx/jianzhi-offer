class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        noCopyStr = []
        count = 0
        if len(s) == 0:
            return count
        if len(s) == 1:
            return count + 1
        for i in s:
            if i not in noCopyStr:
                noCopyStr.append(i)
        count = len(noCopyStr)
        strList = list(s)
        flag = 0
        for i in range(1, len(strList)):
            if strList[0] == strList[i]:
                flag += 1
        if flag >= 1:
            return count
        else: 
            return count - 1
str = "au"
print(len(str))
s = Solution()
print(s.lengthOfLongestSubstring(str))