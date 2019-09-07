# -*- coding:utf-8 -*-
'''


'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []

        for i in pushV:
            stack.append(i):
            while len(stack) != 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            if len(stack):
                return False
            else:
                return True