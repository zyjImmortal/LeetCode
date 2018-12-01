# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        result = ''
        while self:
            result = result + str(self.value) + '->'
            self = self.next
        result = result + 'None'
        return result


class Solution:

    def reverseList(self, head):

        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
    
    def swap_pairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next
    
    
    def has_cycle(self, head):
        # ids = {}
        # while head:
        #     if id(head) in ids:
        #         return True
        #     head = head.next
        # return False
        fast = slow = head
        while fast is not None and slow is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False
            
def map_list_to_linkedlist(seq):
    head = ListNode(None)
    cur = head.next
    for value in seq:
        node = ListNode(value)
        cur= node
        cur = cur.next
    return head



head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)
head.next.next.next = ListNode(7)

linkeds = [3,4,5,6,7,8]
head = map_list_to_linkedlist(linkeds)
print(head)