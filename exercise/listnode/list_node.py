# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = [self.val]
        text = self.next
        while text:
            result.append(text.val)
            text = text.next
        return '->'.join(map(str, result))


class Solution:

    def deleteNode(self, node):
        """
        请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def removeElements(self, head, val):
        """
        删除链表中等于给定值 val 的所有节点。
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        思路：
            新建一个头结点，因为删除的node可能是给定链表的头结点
            通过cur油标指向要比较的节点
            通过pre这个引用操作dummp对象，真正的链表对象
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        pre = dummy
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        pointer = temp
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1 is not None:
            pointer.next = l1
        if l2 is not None:
            pointer.next = l2
        return temp.next

    def reverseList(self, head):
        """
        链表反转
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last

    def deleteDuplicates(self, head):
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。删除重复元素
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head.next
        pre = head
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = head.next
        while cur.next:
            pass


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = 0
        self.next = None

    def __len__(self):
        pre = self
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def __str__(self):
        result = [self.val]
        text = self.next
        while text:
            result.append(text.val)
            text = text.next
        return '->'.join(map(str, result))

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if len(self) < index or index < 0:
            return -1
        pre = self
        while index < 0:
            pre = pre.next
            index -= 1
        return pre

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new = MyLinkedList()
        new.val = val
        new.next = self
        return new

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        val = self._head.elem
        self._head = self._head.next
        return val

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        p = self._head
        if p.next is None:
            elem = p.elem
            p = None
            return elem
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == '__main__':
    nodes = ListNode(5)
    nodes.next = ListNode(6)
    nodes.next.next = ListNode(7)
    nodes.next.next.next = ListNode(7)
    nodes.next.next.next.next = ListNode(8)
    nodes1 = ListNode(1)
    nodes1.next = ListNode(1)
    nodes1.next.next = ListNode(1)
    nodes1.next.next.next = ListNode(3)
    nodes1.next.next.next.next = ListNode(3)
    solution = Solution()
    print(solution.deleteDuplicates(nodes1))
