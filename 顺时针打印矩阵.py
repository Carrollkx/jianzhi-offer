# -*- coding:utf-8 -*-
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix == None:
            return
        if matrix == []:
            return []
        start = 0
        printArray = []
        rows = len(matrix)
        columns = len(matrix[0])
        while columns > 2*start and rows > 2*start:
            endx = columns - 1 - start
            endy = rows - 1 - start
            #从左到右将数字存入
            for i in rang(start, endx+1):
                printArray.append(matrix[start][i])
            for i in range(start+1, endy+1):
                printArray.append(matrix[i][endx])
            for i in range(endx-1, start-1, -1):
                printArray.append(matrix[endy][i])
            for i in range(endy-1, start, -1):
                printArray.append(matrix[i][start])
            start += 1
            return printArray