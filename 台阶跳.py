# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
解题思路：
看做斐波那契函数进行解决
'''
class Solution:
    def jumpFloor(self, number):
        res = [1, 2]
        if number <= 2:
            return number
        else:
            for i in range(3, number + 1):
                res[i%2 - 1] = res[0] + res[1]
            return res[number%2 - 1]