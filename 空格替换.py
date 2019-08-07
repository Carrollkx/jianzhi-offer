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
        return "".join(spacereplace)
if __name__=="__main__":
    REPLACESPACE = Solution()
    s = 'we are happy!'
    print(REPLACESPACE.replace_space(s))