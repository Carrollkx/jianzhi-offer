# -*- coding: utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个+++++非递减排序+++++的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return None
        front = 0
        rear = len(rotateArray) - 1
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[0]
        else:
            while rear - front > 1:
                mid = (rear + front)  // 2
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                elif rotateArray[mid] == rotateArray[front]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < rotateArray[0]:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal
if __name__=="__main__":
    Test = Solution()
    print(Test.minNumberRotateArray([7,8,9,1,2,3,4,5,6]))
    print(Test.minNumberRotateArray([3, 4, 5, 2]))
    print(Test.minNumberRotateArray([1, 1, 1, 0, 1]))
    print(Test.minNumberRotateArray([2, 2, 2, 0, 2]))
    print(Test.minNumberRotateArray([1, 0, 1, 1, 1]))
    print(Test.minNumberRotateArray([]))

                
        