# -*- coding: utf-8 -*-
'''
 输入一个整数，输出该数的二进制表示1的个数，其中负数用补码表示
 例如把9表示成二进制数是1001，有2位是1，因此输入如果是9，则该函数输出是2
'''
class Solution:
    def Numberof1(self, n):
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count
