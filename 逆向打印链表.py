# -*- coding:UTF-8 -*-
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class LNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution:
    def printlistnode(self, LNode):
        if LNode.val is None:
            return
        l = []
        head = LNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l
        
if __name__=="__main__":
    node1 = LNode(10)
    node2 = LNode(20)
    node3 = LNode(30)
    node1.next = node2
    node2.next = node3

    s = Solution()
    print(s.printlistnode(node1))
    
