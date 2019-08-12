#-*- coding:UTF-8 -*-
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    def replace_space(self, s):
        if type(s) is not str:
            return
        spacereplace = []
        for item in s:   
            if item == ' ':
                spacereplace.append('%20')
            else:
                spacereplace.append(item)
        print(type(spacereplace))
        return " ".join(spacereplace)
    def replace_space2(self, s):
        if type(s) is not str:
            return
        spacereplace = []
        s = list(s)
        print(s)
        for i in range(0, len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
if __name__=="__main__":
    REPLACESPACE = Solution()
    s = '1 2 3 '
    print(REPLACESPACE.replace_space(s))
    print(REPLACESPACE.replace_space2(s))