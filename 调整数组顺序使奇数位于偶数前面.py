# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        '''
        数组中奇数和偶数的顺序发生了改变
        '''
        if len(array) < 1:
            return
        elif len(array) = 1:
            return array
        front = 0
        rear = len(array) - 1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array
    def reOrderArray1(self, array):
        if len(array) < 1:
            return
        elif len(array) = 1:
            return array
        arrayodd = []
        arrayeven = []
        for i in array:
            if i & 0x1:
                arrayodd.append(i)
            else:
                arrayeven.append(i)
        return arrayodd+arrayeven
