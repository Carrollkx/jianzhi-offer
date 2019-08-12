# _*_coding:UTF-8_*_
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''

'''
如果出现了array中既有字符串,又有数字,可能需要用到ord()函数,这里就不展开讨论了
'''
class Solution:
    def find(self, array, target):
        if array is None:
            return False
        
        row = len(array[1])
        col = len(array[0])
        print(row)

        if type(target) is not int:
            return False
        
        i = 0
        j = col-1
        while i <= row and j >= 0:
            if array[i][j] < target:
                i += 1
                if i == row:
                    return False
            elif array[i][j] > target:
                j -= 1
                if j == 0:
                    return False
            else:
                return True
        return False
    def Find(self, array, target):
        if array is None:
            return error
        n=len(array)
        for i in range(n):
            print(array[i])
            if target in array[i]:
                print('ok')

if __name__=="__main__":
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    FINDTARGET = Solution()
    print(FINDTARGET.Find(array,9))
